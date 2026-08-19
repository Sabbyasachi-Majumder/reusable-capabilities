"""
Defines supported timestamp presentation formats.
"""

from enum import Enum


class TimestampFormat(Enum):
    """
    Supported timestamp presentation formats.
    """

    STANDARD = "standard"

    BRACKETED = "bracketed"

    PARENTHESIZED = "parenthesized"
