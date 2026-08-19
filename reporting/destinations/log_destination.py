"""
Provides log publishing functionality.

Responsible for resolving session log files
and writing reporting content.
"""

from pathlib import Path

from reporting.config.reporting_config import (
    ReportingConfig,
)
from reporting.models.log_type import (
    LogType,
)
from reporting.services.reporting_session_manager import (
    ReportingSessionManager,
)


class LogDestination:
    """
    Reporting log destination.
    """

    # Publishes content to a log file.
    def publish(
        self,
        content: str,
        log_type: LogType,
    ) -> None:

        if (
            log_type
            == LogType.ALL
        ):

            self.publish(
                content=content,
                log_type=LogType.OPERATIONAL,
            )

            self.publish(
                content=content,
                log_type=LogType.DIAGNOSTIC,
            )

            return

        log_file = (
            self._resolve_log_file(
                log_type
            )
        )

        with open(
            log_file,
            "a",
            encoding="utf-8",
        ) as file:

            file.write(
                content
            )

            file.write(
                "\n"
            )

    # Resolves the destination log file.
    def _resolve_log_file(
        self,
        log_type: LogType,
    ) -> Path:

        root_directory = (
            ReportingConfig.get(
                "logs",
                "root_directory",
            )
        )

        session_prefix = (
            ReportingConfig.get(
                "logs",
                "session_prefix",
            )
        )

        session_id = (
            ReportingSessionManager
            .get_session_id()
        )

        directory_name = (
            ReportingConfig.get(
                "logs",
                f"{log_type.value}_directory",
            )
        )

        log_directory = (
            Path(root_directory)
            / directory_name
        )

        log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return (
            log_directory
            / f"{session_prefix}_{session_id}.log"
        )

    # Runs the destination manually.
    def manual_run(
        self,
    ) -> None:

        session_id = (
            ReportingSessionManager
            .initialize()
        )

        print(
            "\nReporting Session Started"
        )

        print(
            f"Session Id: "
            f"{session_id}"
        )

        while True:

            print(
                "\nLog Types:"
            )

            print(
                "1. Operational"
            )

            print(
                "2. Diagnostic"
            )

            print(
                "0. Exit"
            )

            selection = input(
                "\nSelection: "
            )

            if selection == "0":

                ReportingSessionManager.end_session()

                print(
                    "\nReporting Session Ended"
                )

                break

            if selection == "1":

                log_type = (
                    LogType.OPERATIONAL
                )

            elif selection == "2":

                log_type = (
                    LogType.DIAGNOSTIC
                )

            elif selection == "3":

                log_type = (
                    LogType.ALL
                )

            else:

                print(
                    "\nInvalid selection."
                )

                continue

            content = input(
                "\nContent: "
            )

            self.publish(
                content=content,
                log_type=log_type,
            )

            log_file = (
                self._resolve_log_file(
                    log_type
                )
            )

            print(
                "\nContent written successfully."
            )

            print(
                f"Log File: "
                f"{log_file}"
            )


if __name__ == "__main__":

    LogDestination().manual_run()
