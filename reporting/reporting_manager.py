"""
Central reporting subsystem entry point.

Provides a stable public API for runtime
reporting and structured reporting.
"""

from reporting.destinations.log_destination import (
    LogDestination,
)
from reporting.destinations.terminal_destination import (
    TerminalDestination,
)
from reporting.models.heading_type import (
    HeadingType,
)
from reporting.models.log_type import (
    LogType,
)
from reporting.models.report_destination import (
    ReportDestination,
)

from reporting.artifacts.heading_block import (
    HeadingBlock,
)

from reporting.artifacts.timestamp_block import (
    TimestampBlock,
)
from reporting.artifacts.message_block import (
    MessageBlock,
)

from reporting.models.message_data import (
    MessageData,
)


class ReportingManager:
    """
    Public entry point into the reporting
    subsystem.
    """

    def __init__(
        self,
    ) -> None:

        self._terminal_destination = TerminalDestination()

        self._log_destination = LogDestination()

        self._heading_block = HeadingBlock()

        self._timestamp_block = TimestampBlock()

        self._message_block = MessageBlock()

    # Publishes content to the selected destinations.
    def _publish(
        self,
        content: str,
        destination: ReportDestination = (ReportDestination.LOG),
        log_type: LogType = (LogType.OPERATIONAL),
    ) -> None:

        if destination in (
            ReportDestination.TERMINAL,
            ReportDestination.ALL,
        ):

            self._terminal_destination.publish(content)

        if destination in (
            ReportDestination.LOG,
            ReportDestination.ALL,
        ):

            self._log_destination.publish(
                content=content,
                log_type=log_type,
            )

    # Publishes a heading.
    def _heading(
        self,
        title: str,
        heading_type: HeadingType,
        destination: ReportDestination = (ReportDestination.LOG),
        log_type: LogType = (LogType.OPERATIONAL),
    ) -> None:

        heading_content = self._heading_block.build(
            title=title,
            heading_type=heading_type,
        )

        self._publish(
            content=heading_content.content,
            destination=destination,
            log_type=log_type,
        )

    # Publishes a header.
    def header(
        self,
        title: str,
        destination: ReportDestination = (ReportDestination.LOG),
        log_type: LogType = (LogType.OPERATIONAL),
    ) -> None:

        self._heading(
            title=title,
            heading_type=HeadingType.HEADER,
            destination=destination,
            log_type=log_type,
        )

    # Publishes a sub header.
    def sub_header(
        self,
        title: str,
        destination: ReportDestination = (ReportDestination.LOG),
        log_type: LogType = (LogType.OPERATIONAL),
    ) -> None:

        self._heading(
            title=title,
            heading_type=HeadingType.SUB_HEADER,
            destination=destination,
            log_type=log_type,
        )

    # Publishes a timestamp.
    def timestamp(
        self,
        timestamp_type=None,
        timestamp_format=None,
        component_gap=None,
        destination: ReportDestination = (ReportDestination.LOG),
        log_type: LogType = (LogType.OPERATIONAL),
    ) -> None:

        timestamp_content = self._timestamp_block.build(
            timestamp_type=timestamp_type,
            timestamp_format=timestamp_format,
            component_gap=component_gap,
        )

        self._publish(
            content=timestamp_content,
            destination=destination,
            log_type=log_type,
        )

    # Publishes a message.
    def message(
        self,
        message: str,
        timestamp: bool = False,
        tag: str | None = None,
        data_items: list[MessageData] | None = None,
        destination: ReportDestination = (ReportDestination.LOG),
        log_type: LogType = (LogType.OPERATIONAL),
    ) -> None:

        message_content = self._message_block.build(
            message=message,
            timestamp=timestamp,
            tag=tag,
            data_items=data_items,
        )

        self._publish(
            content=message_content.content,
            destination=destination,
            log_type=log_type,
        )

    # Defines the event reporting contract.
    def event(
        self,
        message: str,
        destination: ReportDestination = (ReportDestination.LOG),
    ) -> None:

        raise NotImplementedError

    # Defines the progress reporting contract.
    def progress(
        self,
        progress,
        destination: ReportDestination = (ReportDestination.LOG),
    ) -> None:

        raise NotImplementedError

    # Defines the table reporting contract.
    def table(
        self,
        table,
        destination: ReportDestination = (ReportDestination.LOG),
    ) -> None:

        raise NotImplementedError

    # Defines the metric reporting contract.
    def metric(
        self,
        metric,
        destination: ReportDestination = (ReportDestination.LOG),
    ) -> None:

        raise NotImplementedError

    # Defines the summary reporting contract.
    def summary(
        self,
        summary,
        destination: ReportDestination = (ReportDestination.LOG),
    ) -> None:

        raise NotImplementedError

    # Defines the diagnostic reporting contract.
    def diagnostic(
        self,
        message: str,
        destination: ReportDestination = (ReportDestination.LOG),
    ) -> None:

        raise NotImplementedError
