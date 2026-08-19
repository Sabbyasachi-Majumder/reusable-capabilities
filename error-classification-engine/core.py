"""
Provides the public entry point for the Error
Classification Engine.

Responsible for orchestrating catalog loading,
message normalization, pattern matching, and
error classification result generation.
"""

from pathlib import Path

from json_loader import JsonLoader
from text_normalizer import TextNormalizer
from pattern_matcher import PatternMatcher
from bootstrap_error_handler import (
    BootstrapErrorHandler,
)


class ErrorClassificationEngine:

    # Builds a fallback response when classification
    # cannot be performed.
    @classmethod
    def _build_fallback_response(
        cls,
        raw_error_message: str,
    ) -> dict:

        return {
            "error_code": "UNKNOWN_ERROR",
            "description": (
                "Error classification could not be performed."
            ),
            "messages": {
                "backend": raw_error_message,
                "frontend": raw_error_message,
                "log": raw_error_message,
            },
            "category": "classification",
            "severity": "warning",
            "diagnostic_logging": True,
        }

    # Classifies a raw error message using the
    # configured error catalog.
    @classmethod
    def classify(
        cls,
        raw_error_message: str,
        error_catalog_path: str | Path,
    ) -> dict:

        try:

            catalog = JsonLoader.load(
                error_catalog_path
            )

        except Exception as error:

            bootstrap_error = (
                BootstrapErrorHandler.resolve(
                    error=error,
                    file_path=error_catalog_path,
                )
            )

            #
            # TODO:
            # Send bootstrap_error to the
            # Reporting Module once integrated.
            #
            # ReportingManager.report(
            #     bootstrap_error
            # )
            #

            return cls._build_fallback_response(
                raw_error_message
            )

        normalized_error_message = (
            TextNormalizer.normalize(
                raw_error_message
            )
        )

        for (
            error_code,
            error_definition,
        ) in catalog.items():

            if (
                error_code
                == "UNKNOWN_ERROR"
            ):
                continue

            matched_pattern = (
                PatternMatcher.match(
                    source=normalized_error_message,
                    candidates=error_definition[
                        "patterns"
                    ],
                )
            )

            if matched_pattern:

                return {
                    "error_code": error_code,
                    "matched_pattern": matched_pattern,
                    **error_definition,
                }

        unknown_error = catalog.get(
            "UNKNOWN_ERROR",
            {
                "description": (
                    "Error could not be classified."
                ),
                "category": "classification",
                "severity": "warning",
                "diagnostic_logging": True,
            },
        )

        return {
            "error_code": "UNKNOWN_ERROR",
            "description": unknown_error[
                "description"
            ],
            "messages": {
                "backend": raw_error_message,
                "frontend": raw_error_message,
                "log": raw_error_message,
            },
            "category": unknown_error[
                "category"
            ],
            "severity": unknown_error[
                "severity"
            ],
            "diagnostic_logging": unknown_error[
                "diagnostic_logging"
            ],
        }
