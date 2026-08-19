"""
Tests bootstrap error handling functionality.

Validates conversion of native exceptions into
diagnostic bootstrap events used during capability
initialization.
"""

import json

from bootstrap_error_handler import (
    BootstrapErrorHandler,
)


# Verifies FileNotFoundError is resolved correctly.
def test_resolve_file_not_found():

    error = FileNotFoundError(
        "File not found"
    )

    result = (
        BootstrapErrorHandler.resolve(
            error=error,
            file_path="catalog.json",
        )
    )

    assert (
        result["error_code"]
        == "FILE_NOT_FOUND"
    )

    assert (
        result["reason"]
        == "File could not be found."
    )

    assert (
        result["file_path"]
        == "catalog.json"
    )

    assert (
        result["native_error"]
        == "File not found"
    )


# Verifies PermissionError is resolved correctly.
def test_resolve_access_denied():

    error = PermissionError(
        "Access denied"
    )

    result = (
        BootstrapErrorHandler.resolve(
            error=error,
            file_path="catalog.json",
        )
    )

    assert (
        result["error_code"]
        == "FILE_ACCESS_DENIED"
    )

    assert (
        result["reason"]
        == "Access to the file was denied."
    )


# Verifies JSONDecodeError is resolved correctly.
def test_resolve_invalid_file_format():

    error = json.JSONDecodeError(
        "Invalid JSON",
        "{}",
        0,
    )

    result = (
        BootstrapErrorHandler.resolve(
            error=error,
            file_path="catalog.json",
        )
    )

    assert (
        result["error_code"]
        == "INVALID_FILE_FORMAT"
    )

    assert (
        result["reason"]
        == "File content could not be parsed."
    )


# Verifies OSError is resolved correctly.
def test_resolve_file_corrupted():

    error = OSError(
        "Unable to read file"
    )

    result = (
        BootstrapErrorHandler.resolve(
            error=error,
            file_path="catalog.json",
        )
    )

    assert (
        result["error_code"]
        == "FILE_CORRUPTED"
    )

    assert (
        result["reason"]
        == "File could not be loaded."
    )


# Verifies unknown exceptions fall back correctly.
def test_resolve_unknown_bootstrap_error():

    error = RuntimeError(
        "Unexpected failure"
    )

    result = (
        BootstrapErrorHandler.resolve(
            error=error,
            file_path="catalog.json",
        )
    )

    assert (
        result["error_code"]
        == "UNKNOWN_ERROR"
    )

    assert (
        result["reason"]
        == "Unexpected failure"
    )

    assert (
        result["native_error"]
        == "Unexpected failure"
    )


# Verifies file path is preserved.
def test_resolve_preserves_file_path():

    error = FileNotFoundError(
        "File not found"
    )

    result = (
        BootstrapErrorHandler.resolve(
            error=error,
            file_path="catalog.json",
        )
    )

    assert (
        result["file_path"]
        == "catalog.json"
    )
