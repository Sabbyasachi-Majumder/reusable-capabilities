"""
Provides reusable text normalization functionality.

Responsible for converting arbitrary text into a
consistent format suitable for matching operations.

Normalization improves matching reliability by
removing formatting differences that do not affect
meaning.
"""

import re


class TextNormalizer:

    _PUNCTUATION_PATTERN = re.compile(
        r"[^\w\s]"
    )

    _WHITESPACE_PATTERN = re.compile(
        r"\s+"
    )

    @classmethod
    def normalize(
        cls,
        text: str,
    ) -> str:
        """
        Normalizes text for matching purposes.
        """

        normalized_text = (
            text.lower()
        )

        normalized_text = (
            cls._PUNCTUATION_PATTERN.sub(
                " ",
                normalized_text,
            )
        )

        normalized_text = (
            cls._WHITESPACE_PATTERN.sub(
                " ",
                normalized_text,
            )
        )

        return (
            normalized_text.strip()
        )
