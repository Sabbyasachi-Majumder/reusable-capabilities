"""
Provides reusable pattern matching functionality.

Responsible for identifying whether a source text
contains any candidate patterns and returning the
best matching pattern.

Matching is deterministic and favors the most
specific pattern by evaluating longer patterns first.
"""


class PatternMatcher:

    @classmethod
    def match(
        cls,
        source: str,
        candidates: list[str],
    ) -> str | None:
        """
        Returns the best matching candidate pattern.

        Matching is performed using complete pattern
        containment rather than token or fuzzy matching.
        """

        sorted_candidates = sorted(
            candidates,
            key=len,
            reverse=True,
        )

        for candidate in sorted_candidates:

            if candidate in source:

                return candidate

        return None
