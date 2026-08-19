"""
Reporting subsystem end-to-end test harness.

Provides interactive validation for
reporting flows, artifacts, and
destinations.
"""

from reporting.reporting_manager import (
    ReportingManager,
)

from reporting.models.log_type import (
    LogType,
)

from reporting.models.report_destination import (
    ReportDestination,
)

from reporting.services.reporting_session_manager import (
    ReportingSessionManager,
)

from reporting.models.timestamp_type import (
    TimestampType,
)

from reporting.models.timestamp_format import (
    TimestampFormat,
)

from reporting.utils.selection_helper import (
    SelectionHelper,
)

from reporting.models.message_data import (
    MessageData,
)


def select_destination(
) -> ReportDestination | None:

    selection = (
        SelectionHelper
        .select_option(
            title="Destinations",
            options=[
                "Terminal",
                "Log",
                "All",
            ],
        )
    )

    if selection is None:

        ReportingSessionManager.end_session()

        return None

    if selection == "Terminal":

        return (
            ReportDestination.TERMINAL
        )

    if selection == "Log":

        return (
            ReportDestination.LOG
        )

    if selection == "All":

        return (
            ReportDestination.ALL
        )

    raise ValueError(
        "Invalid destination."
    )

# Resolves a reporting log type manually.


def select_log_type(
) -> LogType:

    selection = (
        SelectionHelper
        .select_option(
            title="Log Types",
            options=[
                "Operational",
                "Diagnostic",
                "All",
            ],
        )
    )

    if selection is None:

        raise ValueError(
            "Exit selected."
        )

    if selection == "Operational":

        return (
            LogType.OPERATIONAL
        )

    if selection == "Diagnostic":

        return (
            LogType.DIAGNOSTIC
        )

    if selection == "All":

        return (
            LogType.ALL
        )

    raise ValueError(
        "Invalid log type."
    )

# Collects message options manually.


def publish_message(
    manager: ReportingManager,
    destination: ReportDestination,
    log_type: LogType,
) -> None:

    message = input(
        "\nMessage: "
    )

    selection = (
        SelectionHelper
        .select_option(
            title="Include Timestamp",
            options=[
                "Yes",
                "No",
            ],
        )
    )

    if selection is None:

        return

    timestamp = (
        selection == "Yes"
    )

    tag = input(
        "\nTag (Optional): "
    ).strip()

    if not tag:

        tag = None

    data_items: list[
        MessageData
    ] = []

    data_count_input = input(
        "\nData Item Count: "
    ).strip()

    if data_count_input:

        data_count = int(
            data_count_input
        )

        for index in range(
            data_count
        ):

            print(
                f"\nData Item "
                f"{index + 1}"
            )

            label = input(
                "Label: "
            )

            value = input(
                "Value: "
            )

            data_items.append(
                MessageData(
                    label=label,
                    value=value,
                )
            )

    manager.message(
        message=message,
        timestamp=timestamp,
        tag=tag,
        data_items=(
            data_items
            if data_items
            else None
        ),
        destination=destination,
        log_type=log_type,
    )

# Runs a complete reporting flow.


# Runs a complete reporting flow.
def run_reporting_session(
    manager: ReportingManager,
) -> None:

    session_id = (
        ReportingSessionManager
        .initialize()
    )

    print(
        "\nReporting Flow Session Started"
    )

    print(
        f"Session Id: "
        f"{session_id}"
    )

    try:

        destination = (
            select_destination()
        )

        if destination is None:

            return

        log_type = (
            select_log_type()
        )

    except ValueError:

        print(
            "\nInvalid selection."
        )

        ReportingSessionManager.end_session()

        return

    while True:

        operation = (
            SelectionHelper
            .select_option(
                title="Operations",
                options=[
                    "Header",
                    "Sub Header",
                    "Timestamp",
                    "Message",
                ],
            )
        )

        if operation is None:

            ReportingSessionManager.end_session()

            print(
                "\nReporting Flow Session Ended"
            )

            break

        if operation == "Header":

            title = input(
                "\nTitle: "
            )

            manager.header(
                title=title,
                destination=destination,
                log_type=log_type,
            )

        elif operation == "Sub Header":

            title = input(
                "\nTitle: "
            )

            manager.sub_header(
                title=title,
                destination=destination,
                log_type=log_type,
            )

        elif operation == "Timestamp":

            publish_timestamp(
                manager=manager,
                destination=destination,
                log_type=log_type,
            )

        elif operation == "Message":

            publish_message(
                manager=manager,
                destination=destination,
                log_type=log_type,
            )

        else:

            print(
                "\nInvalid operation."
            )

# Collects timestamp options manually.


def publish_timestamp(
    manager: ReportingManager,
    destination: ReportDestination,
    log_type: LogType,
) -> None:

    selection = (
        SelectionHelper
        .select_option(
            title="Timestamp Types",
            options=[
                "Time",
                "Date",
                "Date Time",
            ],
        )
    )

    if selection is None:

        return

    if selection == "Time":

        timestamp_type = (
            TimestampType.TIME
        )

    elif selection == "Date":

        timestamp_type = (
            TimestampType.DATE
        )

    elif selection == "Date Time":

        timestamp_type = (
            TimestampType.DATE_TIME
        )

    else:

        raise ValueError(
            "Invalid timestamp type."
        )

    selection = (
        SelectionHelper
        .select_option(
            title="Formats",
            options=[
                "Standard",
                "Bracketed",
                "Parenthesized",
            ],
        )
    )

    if selection is None:

        return

    if selection == "Standard":

        timestamp_format = (
            TimestampFormat.STANDARD
        )

    elif selection == "Bracketed":

        timestamp_format = (
            TimestampFormat.BRACKETED
        )

    elif selection == "Parenthesized":

        timestamp_format = (
            TimestampFormat.PARENTHESIZED
        )

    else:

        raise ValueError(
            "Invalid timestamp format."
        )

    component_gap = None

    if (
        timestamp_type
        == TimestampType.DATE_TIME
    ):

        selection = (
            SelectionHelper
            .select_option(
                title="Gap Options",
                options=[
                    "Default Gap",
                    "Custom Gap",
                ],
            )
        )

        if selection is None:

            return

        if (
            selection
            == "Custom Gap"
        ):

            component_gap = input(
                "\nCustom Gap: "
            )

    manager.timestamp(
        timestamp_type=timestamp_type,
        timestamp_format=timestamp_format,
        component_gap=component_gap,
        destination=destination,
        log_type=log_type,
    )

# Runs the reporting E2E harness.


# Runs the reporting E2E harness.
def main(
) -> None:

    manager = ReportingManager()

    while True:

        selection = (
            SelectionHelper
            .select_option(
                title="Reporting Manager",
                options=[
                    "Full Reporting Flow",
                    "Heading Block",
                    "Timestamp Block",
                    "Message Block",
                    "Log Destination",
                    "Terminal Destination",
                ],
            )
        )

        if selection is None:

            break

        elif (
            selection
            == "Full Reporting Flow"
        ):

            run_reporting_session(
                manager
            )

        elif (
            selection
            == "Heading Block"
        ):

            manager._heading_block.manual_run()

        elif (
            selection
            == "Timestamp Block"
        ):

            manager._timestamp_block.manual_run()

        elif (
            selection
            == "Message Block"
        ):

            manager._message_block.manual_run()

        elif (
            selection
            == "Log Destination"
        ):

            manager._log_destination.manual_run()

        elif (
            selection
            == "Terminal Destination"
        ):

            manager._terminal_destination.manual_run()


if __name__ == "__main__":

    main()
