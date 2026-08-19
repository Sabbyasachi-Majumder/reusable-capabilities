"""
Generates message content.

Responsible for building structured
reporting messages for runtime output.
"""

from reporting.artifacts.timestamp_block import (
    TimestampBlock,
)
from reporting.config.reporting_config import (
    ReportingConfig,
)
from reporting.models.message_block_content import (
    MessageBlockContent,
)
from reporting.models.message_data import (
    MessageData,
)
from reporting.models.timestamp_format import (
    TimestampFormat,
)
from reporting.models.timestamp_type import (
    TimestampType,
)

from reporting.utils.selection_helper import (
    SelectionHelper,
)


class MessageBlock:
    """
    Message block generator.
    """

    def __init__(
        self,
    ) -> None:

        self._timestamp_block = (
            TimestampBlock()
        )

    # Builds a message block.
    def build(
        self,
        message: str,
        timestamp: bool = False,
        tag: str | None = None,
        data_items: (
            list[MessageData] | None
        ) = None,
    ) -> MessageBlockContent:

        if not message.strip():

            raise ValueError(
                "Message cannot be empty."
            )

        components: list[str] = []

        if timestamp:

            timestamp_content = (
                self._timestamp_block.build(
                    timestamp_type=TimestampType(
                        ReportingConfig.get(
                            "defaults",
                            "message_timestamp_type",
                        )
                    ),
                    timestamp_format=TimestampFormat(
                        ReportingConfig.get(
                            "defaults",
                            "message_timestamp_format",
                        )
                    ),
                )
            )

            components.append(
                timestamp_content
            )

        if tag:

            tag_prefix = (
                ReportingConfig.get(
                    "message",
                    "tag_prefix",
                )
            )

            tag_suffix = (
                ReportingConfig.get(
                    "message",
                    "tag_suffix",
                )
            )

            components.append(
                (
                    f"{tag_prefix}"
                    f"{tag}"
                    f"{tag_suffix}"
                )
            )

        components.append(
            message
        )

        content = " ".join(
            components
        )

        if data_items:

            data_separator = (
                ReportingConfig.get(
                    "message",
                    "data_separator",
                )
            )

            data_item_separator = (
                ReportingConfig.get(
                    "message",
                    "data_item_separator",
                )
            )

            label_value_separator = (
                ReportingConfig.get(
                    "message",
                    "label_value_separator",
                )
            )

            formatted_data = (
                data_item_separator.join(
                    (
                        f"{item.label}"
                        f"{label_value_separator}"
                        f"{item.value}"
                    )
                    for item in data_items
                )
            )

            content = (
                f"{content}"
                f"{data_separator}"
                f"{formatted_data}"
            )

        return MessageBlockContent(
            content=content
        )

    # Runs the artifact manually.
    def manual_run(
        self,
    ) -> None:

        message = input(
            "\nMessage: "
        )

        timestamp_selection = (
            SelectionHelper.select_option(
                title="Include Timestamp",
                options=[
                    "Yes",
                    "No",
                ],
            )
        )

        if timestamp_selection is None:

            return

        timestamp = (
            timestamp_selection
            == "Yes"
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

        if not data_count_input:

            data_count = 0

        else:

            try:

                data_count = int(
                    data_count_input
                )

            except ValueError:

                raise ValueError(
                    "Data item count "
                    "must be a number."
                )

            if data_count < 0:

                raise ValueError(
                    "Data item count "
                    "cannot be negative."
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

        message_content = (
            self.build(
                message=message,
                timestamp=timestamp,
                tag=tag,
                data_items=(
                    data_items
                    if data_items
                    else None
                ),
            )
        )

        print(
            "\nGenerated Message:\n"
        )

        print(
            message_content.content
        )


if __name__ == "__main__":

    MessageBlock().manual_run()
