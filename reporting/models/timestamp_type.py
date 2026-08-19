"""
Defines supported timestamp content types.
"""

from enum import Enum


class TimestampType(Enum):
    """
    Supported timestamp content types.
    """

    DATE = "date"

    TIME = "time"

    DATE_TIME = "date_time"
