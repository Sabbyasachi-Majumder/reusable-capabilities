"""
Provides heading block reporting functionality.

Responsible for heading block formatting,
validation, content generation, and
manual testing support.
"""

from dataclasses import dataclass

from reporting.config.reporting_config import (
    ReportingConfig,
)

from reporting.models.heading_type import (
    HeadingType,
)

from reporting.utils.selection_helper import (
    SelectionHelper,
)


@dataclass(frozen=True)
class HeadingBlockContent:
    """
    Generated heading block content.
    """

    content: str


class HeadingBlock:
    """
    Heading block reporting artifact.
    """

    # Generates heading block content.
    def build(
        self,
        title: str,
        heading_type: HeadingType,
    ) -> HeadingBlockContent:

        self._validate_title(
            title
        )

        formatted_title = (
            self._format_title(
                title=title,
                heading_type=heading_type,
            )
        )

        separator = (
            self._create_separator(
                heading_type=heading_type,
            )
        )

        content = (
            f"{formatted_title}\n"
            f"{separator}"
        )

        return HeadingBlockContent(
            content=content
        )

    # Runs the artifact manually.
    def manual_run(
        self,
    ) -> None:

        title = input(
            "Title: "
        )

        selection = (
            SelectionHelper
            .select_option(
                title="Heading Types",
                options=[
                    "Header",
                    "Sub Header",
                ],
            )
        )

        if selection is None:

            return

        if selection == "Header":

            heading_type = (
                HeadingType.HEADER
            )

        elif selection == "Sub Header":

            heading_type = (
                HeadingType.SUB_HEADER
            )

        else:

            raise ValueError(
                "Invalid selection."
            )

        heading_content = (
            self.build(
                title=title,
                heading_type=heading_type,
            )
        )

        print(
            "\nGenerated Heading:\n"
        )

        print(
            heading_content.content
        )

    # Validates heading input.
    def _validate_title(
        self,
        title: str,
    ) -> None:

        if not title.strip():

            raise ValueError(
                "Title cannot be empty."
            )

    # Formats the heading title.
    def _format_title(
        self,
        title: str,
        heading_type: HeadingType,
    ) -> str:

        width = ReportingConfig.get(
            heading_type.value,
            "width",
        )

        uppercase = ReportingConfig.get(
            heading_type.value,
            "uppercase",
        )

        centered = ReportingConfig.get(
            heading_type.value,
            "center",
        )

        formatted_title = (
            title.upper()
            if uppercase
            else title
        )

        if centered:

            return formatted_title.center(
                width
            )

        return formatted_title

    # Creates the heading separator.
    def _create_separator(
        self,
        heading_type: HeadingType,
    ) -> str:

        width = ReportingConfig.get(
            heading_type.value,
            "width",
        )

        separator = ReportingConfig.get(
            heading_type.value,
            "separator",
        )

        return (
            separator
            * width
        )


if __name__ == "__main__":

    HeadingBlock().manual_run()
