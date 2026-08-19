"""
Tests the reusable JSON loading capability.

Validates successful loading, file existence checks,
path resolution, and native exception propagation.
"""

from pathlib import Path
import json

import pytest

from json_loader import JsonLoader


# Verifies valid JSON files are loaded successfully.
def test_load_valid_json(
    tmp_path: Path,
):

    json_file = (
        tmp_path
        / "sample.json"
    )

    json_file.write_text(
        '{"name": "ArchiveFlow"}',
        encoding="utf-8"
    )

    result = JsonLoader.load(
        json_file
    )

    assert result == {
        "name": "ArchiveFlow"
    }


# Verifies missing files propagate FileNotFoundError.
def test_load_missing_file():

    with pytest.raises(
        FileNotFoundError
    ):

        JsonLoader.load(
            "does_not_exist.json"
        )


# Verifies malformed JSON propagates JSONDecodeError.
def test_load_invalid_json(
    tmp_path: Path,
):

    json_file = (
        tmp_path
        / "invalid.json"
    )

    json_file.write_text(
        '{"name": }',
        encoding="utf-8"
    )

    with pytest.raises(
        json.JSONDecodeError
    ):

        JsonLoader.load(
            json_file
        )


# Verifies exists() returns True for existing files.
def test_exists_returns_true(
    tmp_path: Path,
):

    json_file = (
        tmp_path
        / "sample.json"
    )

    json_file.write_text(
        "{}",
        encoding="utf-8"
    )

    assert (
        JsonLoader.exists(
            json_file
        )
        is True
    )


# Verifies exists() returns False for missing files.
def test_exists_returns_false():

    assert (
        JsonLoader.exists(
            "missing.json"
        )
        is False
    )


# Verifies get_path() returns a Path instance.
def test_get_path_returns_path():

    result = JsonLoader.get_path(
        "sample.json"
    )

    assert isinstance(
        result,
        Path
    )

    assert result == Path(
        "sample.json"
    )
