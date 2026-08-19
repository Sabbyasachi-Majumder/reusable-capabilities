"""
Defines structured message data.

Represents a label and value pair used
within message reporting artifacts.
"""

from dataclasses import dataclass


@dataclass(
    frozen=True
)
class MessageData:
    """
    Structured message data.
    """

    label: str

    value: str

    def __post_init__(
        self,
    ) -> None:

        if not self.label.strip():

            raise ValueError(
                "Label cannot be empty."
            )

        if not self.value.strip():

            raise ValueError(
                "Value cannot be empty."
            )
