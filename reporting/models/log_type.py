"""
Defines supported reporting log types.
"""

from enum import Enum


class LogType(Enum):
    """
    Supported reporting log types.
    """
    ALL = "all"

    OPERATIONAL = "operational"

    DIAGNOSTIC = "diagnostic"
