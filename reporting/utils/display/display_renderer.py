"""
Provides lightweight reusable terminal rendering
utilities for operational metrics and telemetry.
The renderer is generic and not tied to any
specific workflow or execution stage.
Responsible only for low-level
mutable viewport rendering.
"""

import sys
import time


class DisplayRenderer:
    """
    Lightweight terminal metric renderer.
    """

    def __init__(
        self,
        refresh_interval_seconds: float = 0.25,
    ):
        self.refresh_interval_seconds = (
            refresh_interval_seconds
        )

        self.last_render_time = 0.0

    # Renders terminal metrics.
    def render(
        self,
        **metrics,
    ):
        current_time = time.time()

        if (
            current_time
            - self.last_render_time
            < self.refresh_interval_seconds
        ):
            return

        self.last_render_time = (
            current_time
        )

        output = "\n\n".join(
            [
                f"{key}: {value}"
                for key, value
                in metrics.items()
            ]
        )

        sys.stdout.write(
            "\r" + output
        )

        sys.stdout.flush()

    # Completes rendering and moves cursor.
    def complete(self):
        sys.stdout.write("\n")
        sys.stdout.flush()
