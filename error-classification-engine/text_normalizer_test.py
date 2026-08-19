"""
Tests text normalization functionality.

Validates normalization behavior used by the
Error Classification Engine matching process.
"""

from text_normalizer import (
    TextNormalizer,
)


# Verifies lowercase conversion.
def test_lowercase_conversion():

    result = (
        TextNormalizer.normalize(
            "ACCESS DENIED"
        )
    )

    assert (
        result
        == "access denied"
    )


# Verifies leading and trailing whitespace removal.
def test_whitespace_trimming():

    result = (
        TextNormalizer.normalize(
            "   access denied   "
        )
    )

    assert (
        result
        == "access denied"
    )


# Verifies repeated whitespace collapsing.
def test_multiple_space_collapse():

    result = (
        TextNormalizer.normalize(
            "access      denied"
        )
    )

    assert (
        result
        == "access denied"
    )


# Verifies punctuation removal.
def test_punctuation_removal():

    result = (
        TextNormalizer.normalize(
            "PermissionError: [Errno 13] Permission denied."
        )
    )

    assert (
        result
        == "permissionerror errno 13 permission denied"
    )


# Verifies empty strings remain valid.
def test_empty_string():

    result = (
        TextNormalizer.normalize(
            ""
        )
    )

    assert (
        result
        == ""
    )


# Verifies already normalized text is unchanged.
def test_already_normalized_string():

    result = (
        TextNormalizer.normalize(
            "access denied"
        )
    )

    assert (
        result
        == "access denied"
    )


# Verifies newline normalization.
def test_newline_normalization():

    result = (
        TextNormalizer.normalize(
            "access\n\ndenied"
        )
    )

    assert (
        result
        == "access denied"
    )


# Verifies tab normalization.
def test_tab_normalization():

    result = (
        TextNormalizer.normalize(
            "access\t\tdenied"
        )
    )

    assert (
        result
        == "access denied"
    )
