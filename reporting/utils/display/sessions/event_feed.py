"""
Provides append-only semantic event
stream rendering for terminal sessions.
"""


class EventFeed:
    """
    Renders persistent event lines.
    """

    # Writes a semantic event line.
    def write(
        self,
        message: str,
    ) -> None:

        print(
            message,
            flush=True,
        )
