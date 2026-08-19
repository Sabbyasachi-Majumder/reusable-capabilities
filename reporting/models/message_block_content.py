"""
Defines generated message block content.

Represents the generated output produced
by the MessageBlock artifact.
"""

from dataclasses import dataclass


@dataclass(
    frozen=True
)
class MessageBlockContent:
    """
    Generated message block content.
    """

    content: str

    def __post_init__(
        self,
    ) -> None:

        if not self.content.strip():

            raise ValueError(
                "Content cannot be empty."
            )
