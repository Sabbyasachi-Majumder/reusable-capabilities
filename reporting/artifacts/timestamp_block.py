"""
Builds timestamp reporting artifacts.

Provides reusable timestamp generation
for reporting components and destinations.
Supports multiple timestamp types and
presentation formats.
"""

from datetime import datetime

from reporting.models.timestamp_format import (
    TimestampFormat,
)

from reporting.models.timestamp_type import (
    TimestampType,
)

from reporting.config.reporting_config import (
    ReportingConfig,
)

from reporting.utils.selection_helper import (
    SelectionHelper,
)


class TimestampBlock:
    """
    Builds timestamp artifacts.
    """

    # Resolves timestamp content.
    def _resolve_content(
        self,
        timestamp_type: TimestampType,
        component_gap: (
            str | None
        ) = None,
    ) -> str:

        now = datetime.now()

        if (
            timestamp_type
            == TimestampType.TIME
        ):

            return now.strftime(
                ReportingConfig.get(
                    "timestamp",
                    "time_format",
                )
            )

        if (
            timestamp_type
            == TimestampType.DATE
        ):

            return now.strftime(
                ReportingConfig.get(
                    "timestamp",
                    "date_format",
                )
            )

        if (
            timestamp_type
            == TimestampType.DATE_TIME
        ):

            component_gap = (
                self._resolve_gap(
                    component_gap
                )
            )

            date = now.strftime(
                ReportingConfig.get(
                    "timestamp",
                    "date_format",
                )
            )

            time = now.strftime(
                ReportingConfig.get(
                    "timestamp",
                    "time_format",
                )
            )

            return (
                f"{date}"
                f"{component_gap}"
                f"{time}"
            )
        raise ValueError(
            f"Unsupported timestamp "
            f"type: {timestamp_type}"
        )

    # Applies timestamp formatting.
    def _apply_format(
        self,
        content: str,
        timestamp_format: (
            TimestampFormat
        ),
    ) -> str:

        if (
            timestamp_format
            == TimestampFormat.STANDARD
        ):

            return content

        if (
            timestamp_format
            == TimestampFormat.BRACKETED
        ):

            return (
                f"[{content}]"
            )

        if (
            timestamp_format
            == TimestampFormat.PARENTHESIZED
        ):

            return (
                f"({content})"
            )

        raise ValueError(
            f"Unsupported timestamp "
            f"format: "
            f"{timestamp_format}"
        )

    # Resolves default timestamp format.
    def _resolve_format(
        self,
        timestamp_format: (
            TimestampFormat | None
        ),
    ) -> TimestampFormat:

        if timestamp_format is not None:

            return timestamp_format

        configured_format = (
            ReportingConfig.get(
                "defaults",
                "timestamp_format",
            )
        )

        return TimestampFormat(
            configured_format
        )

    # Resolves default timestamp type.
    def _resolve_type(
        self,
        timestamp_type: (
            TimestampType | None
        ),
    ) -> TimestampType:

        if timestamp_type is not None:

            return timestamp_type

        configured_type = (
            ReportingConfig.get(
                "defaults",
                "timestamp_type",
            )
        )

        return TimestampType(
            configured_type
        )

    # Resolves component gap.
    def _resolve_gap(
        self,
        component_gap: (
            str | None
        ),
    ) -> str:

        if component_gap is not None:

            return component_gap

        return ReportingConfig.get(
            "defaults",
            "component_gap",
        )

    # Builds timestamp content.
    def build(
        self,
        timestamp_type: (
            TimestampType | None
        ) = None,
        timestamp_format: (
            TimestampFormat | None
        ) = None,
        component_gap: (
            str | None
        ) = None,
    ) -> str:

        timestamp_type = (
            self._resolve_type(
                timestamp_type
            )
        )

        timestamp_format = (
            self._resolve_format(
                timestamp_format
            )
        )

        component_gap = (
            self._resolve_gap(
                component_gap
            )
        )

        content = (
            self._resolve_content(
                timestamp_type,
                component_gap,
            )
        )

        return self._apply_format(
            content,
            timestamp_format,
        )

    # Runs manual artifact testing.
    def manual_run(
        self,
    ) -> None:

        type_selection = (
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

        if type_selection is None:

            return

        if (
            type_selection
            == "Time"
        ):

            timestamp_type = (
                TimestampType.TIME
            )

        elif (
            type_selection
            == "Date"
        ):

            timestamp_type = (
                TimestampType.DATE
            )

        elif (
            type_selection
            == "Date Time"
        ):

            timestamp_type = (
                TimestampType.DATE_TIME
            )

        else:

            raise ValueError(
                "Invalid timestamp type."
            )

        format_selection = (
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

        if format_selection is None:

            return

        if (
            format_selection
            == "Standard"
        ):

            timestamp_format = (
                TimestampFormat.STANDARD
            )

        elif (
            format_selection
            == "Bracketed"
        ):

            timestamp_format = (
                TimestampFormat.BRACKETED
            )

        elif (
            format_selection
            == "Parenthesized"
        ):

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

            gap_selection = (
                SelectionHelper
                .select_option(
                    title="Gap Options",
                    options=[
                        "Default Gap",
                        "Custom Gap",
                    ],
                )
            )

            if gap_selection is None:

                return

            if (
                gap_selection
                == "Custom Gap"
            ):

                component_gap = input(
                    "\nCustom Gap: "
                )

        timestamp = self.build(
            timestamp_type=timestamp_type,
            timestamp_format=(
                timestamp_format
            ),
            component_gap=(
                component_gap
            ),
        )

        print(
            "\nGenerated Timestamp:\n"
        )

        print(
            timestamp
        )


if __name__ == "__main__":

    TimestampBlock().manual_run()
