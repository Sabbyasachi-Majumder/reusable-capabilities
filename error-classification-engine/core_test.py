"""
Tests the Error Classification Engine.

Validates end-to-end classification behavior,
bootstrap error handling, and UNKNOWN_ERROR
fallback behavior.
"""

import json

from core import (
    ErrorClassificationEngine,
)


# Verifies a known error is classified successfully.
def test_classify_known_error(
    tmp_path,
):

    catalog = {
        "ACCESS_DENIED": {
            "description": (
                "Access denied."
            ),
            "messages": {
                "backend": "backend",
                "frontend": "frontend",
                "log": "log",
            },
            "category": "filesystem",
            "severity": "warning",
            "patterns": [
                "permission denied"
            ],
            "rerun": False,
        },
        "UNKNOWN_ERROR": {
            "description": (
                "Unknown error."
            ),
            "category": (
                "classification"
            ),
            "severity": (
                "warning"
            ),
            "diagnostic_logging": True,
        },
    }

    catalog_file = (
        tmp_path
        / "catalog.json"
    )

    catalog_file.write_text(
        json.dumps(catalog),
        encoding="utf-8",
    )

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=(
                "Permission denied while opening file."
            ),
            error_catalog_path=catalog_file,
        )
    )

    assert (
        result["error_code"]
        == "ACCESS_DENIED"
    )


# Verifies UNKNOWN_ERROR is returned when no match exists.
def test_classify_unknown_error(
    tmp_path,
):

    catalog = {
        "ACCESS_DENIED": {
            "description": (
                "Access denied."
            ),
            "messages": {
                "backend": "backend",
                "frontend": "frontend",
                "log": "log",
            },
            "category": "filesystem",
            "severity": "warning",
            "patterns": [
                "permission denied"
            ],
            "rerun": False,
        },
        "UNKNOWN_ERROR": {
            "description": (
                "Unknown error."
            ),
            "category": (
                "classification"
            ),
            "severity": (
                "warning"
            ),
            "diagnostic_logging": True,
        },
    }

    catalog_file = (
        tmp_path
        / "catalog.json"
    )

    catalog_file.write_text(
        json.dumps(catalog),
        encoding="utf-8",
    )

    raw_error = (
        "Some completely new error."
    )

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=raw_error,
            error_catalog_path=catalog_file,
        )
    )

    assert (
        result["error_code"]
        == "UNKNOWN_ERROR"
    )

    assert (
        result["messages"]["backend"]
        == raw_error
    )

    assert (
        result["messages"]["frontend"]
        == raw_error
    )

    assert (
        result["messages"]["log"]
        == raw_error
    )


def test_catalog_file_not_found():

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=(
                "Permission denied"
            ),
            error_catalog_path=(
                "missing_catalog.json"
            ),
        )
    )

    assert (
        result["error_code"]
        == "UNKNOWN_ERROR"
    )

    assert (
        result["messages"]["backend"]
        == "Permission denied"
    )

    assert (
        result["category"]
        == "classification"
    )


def test_invalid_catalog_format(
    tmp_path,
):

    catalog_file = (
        tmp_path
        / "catalog.json"
    )

    catalog_file.write_text(
        '{"invalid": }',
        encoding="utf-8",
    )

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=(
                "Permission denied"
            ),
            error_catalog_path=catalog_file,
        )
    )

    assert (
        result["error_code"]
        == "UNKNOWN_ERROR"
    )

    assert (
        result["messages"]["backend"]
        == "Permission denied"
    )

    assert (
        result["category"]
        == "classification"
    )


# Verifies message normalization participates in matching.
def test_normalization_before_matching(
    tmp_path,
):

    catalog = {
        "ACCESS_DENIED": {
            "description": (
                "Access denied."
            ),
            "messages": {
                "backend": "backend",
                "frontend": "frontend",
                "log": "log",
            },
            "category": "filesystem",
            "severity": "warning",
            "patterns": [
                "permission denied"
            ],
            "rerun": False,
        },
        "UNKNOWN_ERROR": {
            "description": (
                "Unknown error."
            ),
            "category": (
                "classification"
            ),
            "severity": (
                "warning"
            ),
            "diagnostic_logging": True,
        },
    }

    catalog_file = (
        tmp_path
        / "catalog.json"
    )

    catalog_file.write_text(
        json.dumps(catalog),
        encoding="utf-8",
    )

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=(
                "PERMISSION DENIED!!!"
            ),
            error_catalog_path=catalog_file,
        )
    )

    assert (
        result["error_code"]
        == "ACCESS_DENIED"
    )


# Verifies longest pattern wins through orchestration.
def test_longest_pattern_match(
    tmp_path,
):

    catalog = {
        "FILE_LOCKED": {
            "description": (
                "File locked."
            ),
            "messages": {
                "backend": "backend",
                "frontend": "frontend",
                "log": "log",
            },
            "category": "filesystem",
            "severity": "warning",
            "patterns": [
                "process",
                "being used by another process",
            ],
            "rerun": False,
        },
        "UNKNOWN_ERROR": {
            "description": (
                "Unknown error."
            ),
            "category": (
                "classification"
            ),
            "severity": (
                "warning"
            ),
            "diagnostic_logging": True,
        },
    }

    catalog_file = (
        tmp_path
        / "catalog.json"
    )

    catalog_file.write_text(
        json.dumps(catalog),
        encoding="utf-8",
    )

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=(
                "The file is being used by another process."
            ),
            error_catalog_path=catalog_file,
        )
    )

    assert (
        result["error_code"]
        == "FILE_LOCKED"
    )

# Verifies matched_pattern is returned
# for successful classifications.


def test_matched_pattern_returned(
    tmp_path,
):

    catalog = {
        "ACCESS_DENIED": {
            "description": (
                "Access denied."
            ),
            "messages": {
                "backend": "backend",
                "frontend": "frontend",
                "log": "log",
            },
            "category": "filesystem",
            "severity": "warning",
            "patterns": [
                "permission denied"
            ],
            "rerun": False,
        },
        "UNKNOWN_ERROR": {
            "description": (
                "Unknown error."
            ),
            "category": (
                "classification"
            ),
            "severity": (
                "warning"
            ),
            "diagnostic_logging": True,
        },
    }

    catalog_file = (
        tmp_path
        / "catalog.json"
    )

    catalog_file.write_text(
        json.dumps(catalog),
        encoding="utf-8",
    )

    result = (
        ErrorClassificationEngine.classify(
            raw_error_message=(
                "Permission denied while opening file."
            ),
            error_catalog_path=catalog_file,
        )
    )

    assert (
        result["matched_pattern"]
        == "permission denied"
    )
