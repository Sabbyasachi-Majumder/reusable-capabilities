"""
Provides reporting configuration loading.

Responsible for loading reporting defaults
and exposing configuration values.
"""

import json
from pathlib import Path


class ReportingConfig:
    """
    Reporting configuration loader.
    """

    _config = None

    # Loads reporting configuration.
    @classmethod
    def load(cls) -> None:

        if cls._config is not None:
            return

        config_file = (
            Path(__file__).parent
            / "reporting_defaults.json"
        )

        with open(
            config_file,
            "r",
            encoding="utf-8",
        ) as file:

            cls._config = json.load(
                file
            )

    # Returns a configuration value.
    @classmethod
    def get(
        cls,
        section: str,
        key: str,
    ):

        cls.load()

        return cls._config[
            section
        ][
            key
        ]


if __name__ == "__main__":
    print(
        ReportingConfig.get(
            "header",
            "width",
        )
    )
