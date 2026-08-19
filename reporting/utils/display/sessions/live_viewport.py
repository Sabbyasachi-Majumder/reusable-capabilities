"""
Provides mutable live session viewport
rendering for terminal status summaries.
"""

import time

from reporting.utils.display.display_renderer import (
    DisplayRenderer,
)


class LiveViewport:
    """
    Renders throttled live session state.
    """

    def __init__(
        self,
        refresh_interval_seconds: float = 0.2,
    ):
        self.renderer = DisplayRenderer()

        self.refresh_interval_seconds = refresh_interval_seconds

        self.last_render_time = 0.0

    # Renders the live status viewport.
    def render(
        self,
        **values,
    ) -> None:

        current_time = time.time()

        if current_time - self.last_render_time < self.refresh_interval_seconds:
            return

        self.last_render_time = current_time

        print("\n" + ("-" * 60))

        self.renderer.render(**values)

        print()

    # Completes viewport rendering.
    def complete(
        self,
    ) -> None:

        self.renderer.complete()
