"""
Coordinates semantic event feed rendering
and live session viewport rendering.
"""

from reporting.utils.display.sessions.event_feed import (
    EventFeed,
)

from reporting.utils.display.sessions.live_viewport import (
    LiveViewport,
)


class SessionRenderer:
    """
    Coordinates terminal session rendering.
    """

    def __init__(
        self,
    ):
        self.event_feed = EventFeed()

        self.live_viewport = LiveViewport()

    # Writes a persistent semantic event.
    def event(
        self,
        message: str,
    ) -> None:

        self.event_feed.write(message)

    # Updates live session state.
    def viewport(
        self,
        **values,
    ) -> None:

        self.live_viewport.render(**values)

    # Completes session rendering.
    def complete(
        self,
    ) -> None:

        self.live_viewport.complete()
