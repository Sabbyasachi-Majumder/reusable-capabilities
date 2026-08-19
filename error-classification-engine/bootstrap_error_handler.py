"""
Provides bootstrap error handling functionality.

Responsible for resolving initialization and
dependency-loading failures before the main
Error Catalog becomes available.

Bootstrap errors are intended for internal
diagnostic reporting only.
"""


from pathlib import Path
import json


class BootstrapErrorHandler:

    _ERRORS = {
        FileNotFoundError: {
            "error_code": "FILE_NOT_FOUND",
            "reason": (
                "File could not be found."
            ),
        },
        PermissionError: {
            "error_code": "FILE_ACCESS_DENIED",
            "reason": (
                "Access to the file was denied."
            ),
        },
        json.JSONDecodeError: {
            "error_code": "INVALID_FILE_FORMAT",
            "reason": (
                "File content could not be parsed."
            ),
        },
        OSError: {
            "error_code": "FILE_CORRUPTED",
            "reason": (
                "File could not be loaded."
            ),
        },
    }

    _DEFAULT_ERROR = {
        "error_code": "UNKNOWN_ERROR",
    }

    @classmethod
    def resolve(
        cls,
        error: Exception,
        file_path: str | Path,
    ) -> dict:
        """
        Resolves a native exception into a
        diagnostic bootstrap event.
        """

        error_definition = (
            cls._ERRORS.get(
                type(error),
                cls._DEFAULT_ERROR,
            )
        )

        return {
            "error_code": error_definition[
                "error_code"
            ],
            "reason": (
                error_definition.get(
                    "reason",
                    str(error)
                )
            ),
            "file_path": str(
                file_path
            ),
            "native_error": str(
                error
            ),
        }
