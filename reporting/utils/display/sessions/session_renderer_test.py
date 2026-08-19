"""
Validates session renderer coordination
behavior for event feed and viewport
rendering.
"""

from reporting.utils.display.sessions.session_renderer import (
    SessionRenderer,
)


def test_create_session_renderer():

    renderer = SessionRenderer()

    assert renderer.event_feed is not None

    assert renderer.live_viewport is not None
