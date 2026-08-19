"""
Provides reusable formatting helpers for terminal
display and operational telemetry rendering.
The module focuses purely on value formatting and
contains no rendering or terminal interaction logic.
"""


# Formats integers using comma separators.
def format_number(
    value: int,
) -> str:
    return f"{value:,}"


# Formats byte sizes into readable units.
def format_size(
    size_bytes: int,
) -> str:
    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
    ]

    size = float(size_bytes)

    for unit in units:

        if size < 1024:
            return (
                f"{size:.2f} "
                f"{unit}"
            )

        size /= 1024

    return (
        f"{size:.2f} PB"
    )


# Formats fraction values.
def format_fraction(
    current: int,
    total: int,
) -> str:
    return (
        f"{current:,}"
        f"/"
        f"{total:,}"
    )


# Formats percentage values.
def format_percentage(
    current: int,
    total: int,
) -> str:
    if total == 0:
        return "0.00%"

    percentage = (
        current / total
    ) * 100

    return (
        f"{percentage:.2f}%"
    )


# Formats duration seconds into readable output.
def format_duration(
    seconds: float,
) -> str:
    seconds = int(seconds)

    hours = seconds // 3600

    minutes = (
        seconds % 3600
    ) // 60

    remaining_seconds = (
        seconds % 60
    )

    return (
        f"{hours:02d}:"
        f"{minutes:02d}:"
        f"{remaining_seconds:02d}"
    )
