"""
Validates display formatting utilities.
"""

from reporting.utils.display.display_formatter import (
    format_duration,
    format_fraction,
    format_number,
    format_percentage,
    format_size,
)


def test_format_number():
    assert format_number(301415) == "301,415"


def test_format_size():
    assert format_size(1024) == "1.00 KB"


def test_format_fraction():
    assert format_fraction(4, 12) == "4/12"


def test_format_percentage():
    assert format_percentage(25, 100) == "25.00%"


def test_format_duration():
    assert format_duration(3661) == "01:01:01"
