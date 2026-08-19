"""
Tests pattern matching functionality.

Validates best-match selection, longest-pattern
priority, and no-match scenarios.
"""

from pattern_matcher import (
    PatternMatcher,
)

# Verifies an exact pattern match is found.


def test_exact_pattern_match():

    result = (
        PatternMatcher.match(
            source="permission denied",
            candidates=[
                "permission denied",
                "access denied",
            ],
        )
    )

    assert (
        result
        == "permission denied"
    )


# Verifies a contained pattern is found.
def test_contained_pattern_match():

    result = (
        PatternMatcher.match(
            source=(
                "permission denied while opening file"
            ),
            candidates=[
                "permission denied",
                "access denied",
            ],
        )
    )

    assert (
        result
        == "permission denied"
    )


# Verifies longest matching pattern wins.
def test_longest_pattern_wins():

    result = (
        PatternMatcher.match(
            source=(
                "the process cannot access the file "
                "because it is being used by another process"
            ),
            candidates=[
                "process",
                "another process",
                "being used by another process",
            ],
        )
    )

    assert (
        result
        == "being used by another process"
    )


# Verifies no match returns None.
def test_no_match_returns_none():

    result = (
        PatternMatcher.match(
            source="network timeout",
            candidates=[
                "permission denied",
                "access denied",
            ],
        )
    )

    assert (
        result
        is None
    )


# Verifies empty candidate list returns None.
def test_empty_candidates_returns_none():

    result = (
        PatternMatcher.match(
            source="permission denied",
            candidates=[],
        )
    )

    assert (
        result
        is None
    )


# Verifies empty source returns None.
def test_empty_source_returns_none():

    result = (
        PatternMatcher.match(
            source="",
            candidates=[
                "permission denied",
            ],
        )
    )

    assert (
        result
        is None
    )


# Verifies first matching pattern wins when
# multiple candidates have equal length.
def test_first_equal_length_match_wins():

    result = (
        PatternMatcher.match(
            source=(
                "permission denied and access denied"
            ),
            candidates=[
                "permission denied",
                "access denied",
            ],
        )
    )

    assert (
        result
        == "permission denied"
    )


# Verifies matching is case-sensitive.
# TextNormalizer is expected to normalize first.
def test_matching_requires_normalized_input():

    result = (
        PatternMatcher.match(
            source="Permission Denied",
            candidates=[
                "permission denied",
            ],
        )
    )

    assert (
        result
        is None
    )
