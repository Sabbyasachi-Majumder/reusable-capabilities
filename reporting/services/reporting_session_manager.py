"""
Provides centralized reporting session lifecycle management.

Maintains a single active reporting session that is shared
across all reporting destinations during application execution.
"""

from datetime import datetime


class ReportingSessionManager:

    _session_id: str | None = None

    # Initializes the active reporting session.
    @classmethod
    def initialize(
        cls,
        session_id: str | None = None,
    ) -> str:

        if cls._session_id is None:

            cls._session_id = (
                session_id
                or datetime.now().strftime(
                    "%Y%m%d_%H%M%S_%f"
                )
            )
        return cls._session_id

    # Returns the active session id.
    @classmethod
    def get_session_id(
        cls,
    ) -> str:

        if cls._session_id is None:
            return cls.initialize()

        return cls._session_id

    # Returns the active session id without creating one.
    @classmethod
    def peek_session_id(
        cls,
    ) -> str | None:

        return cls._session_id

    # Clears the active session.
    @classmethod
    def end_session(
        cls,
    ) -> None:

        cls._session_id = None
