"""
Validates logging session lifecycle behavior.
"""

from reporting.services.reporting_session_manager import (
    ReportingSessionManager,
)


def test_session_reuse():

    ReportingSessionManager.end_session()

    session_one = (
        ReportingSessionManager.initialize()
    )

    session_two = (
        ReportingSessionManager.get_session_id()
    )

    assert (
        session_one
        == session_two
    )


def test_session_end_session():

    ReportingSessionManager.initialize()

    ReportingSessionManager.end_session()

    assert (
        ReportingSessionManager.peek_session_id()
        is None
    )


def test_custom_session_id():

    ReportingSessionManager.end_session()

    session_id = (
        ReportingSessionManager.initialize(
            "custom_session"
        )
    )

    assert (
        session_id
        == "custom_session"
    )
