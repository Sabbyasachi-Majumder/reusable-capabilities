"""
Provides reusable JSON file loading functionality.

Responsible for loading and parsing JSON files
from a supplied path.

Raises native exceptions when loading or parsing
fails.
"""


from pathlib import Path
import json


class JsonLoader:

    @classmethod
    def load(
        cls,
        json_path: str | Path,
    ) -> dict:

        file_path = Path(
            json_path
        )

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(
                file
            )

    @classmethod
    def exists(
        cls,
        json_path: str | Path,
    ) -> bool:

        return Path(
            json_path
        ).exists()

    @classmethod
    def get_path(
        cls,
        json_path: str | Path,
    ) -> Path:

        return Path(
            json_path
        )
