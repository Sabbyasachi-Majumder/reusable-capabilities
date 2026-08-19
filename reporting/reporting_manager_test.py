"""
Verifies reporting manager contract.
"""

import pytest

from reporting.reporting_manager import (
    ReportingManager,
)

from reporting.models.report_destination import (
    ReportDestination,
)


# Verifies header publishing.
def test_header():

    manager = ReportingManager()

    manager.header(
        title="SCAN STAGE",
        destination=(
            ReportDestination.TERMINAL
        ),
    )


# Verifies sub header publishing.
def test_sub_header():

    manager = ReportingManager()

    manager.sub_header(
        title="Boundary Planning",
        destination=(
            ReportDestination.TERMINAL
        ),
    )


# Verifies event contract.
def test_event_not_implemented():

    manager = ReportingManager()

    with pytest.raises(
        NotImplementedError
    ):
        manager.event(
            message="Test",
            destination=(
                ReportDestination.ALL
            ),
        )


# Verifies progress contract.
def test_progress_not_implemented():

    manager = ReportingManager()

    with pytest.raises(
        NotImplementedError
    ):
        manager.progress(
            progress=None,
            destination=(
                ReportDestination.ALL
            ),
        )


# Verifies table contract.
def test_table_not_implemented():

    manager = ReportingManager()

    with pytest.raises(
        NotImplementedError
    ):
        manager.table(
            table=None,
            destination=(
                ReportDestination.ALL
            ),
        )


# Verifies metric contract.
def test_metric_not_implemented():

    manager = ReportingManager()

    with pytest.raises(
        NotImplementedError
    ):
        manager.metric(
            metric=None,
            destination=(
                ReportDestination.ALL
            ),
        )


# Verifies summary contract.
def test_summary_not_implemented():

    manager = ReportingManager()

    with pytest.raises(
        NotImplementedError
    ):
        manager.summary(
            summary=None,
            destination=(
                ReportDestination.ALL
            ),
        )


# Verifies diagnostic contract.
def test_diagnostic_not_implemented():

    manager = ReportingManager()

    with pytest.raises(
        NotImplementedError
    ):
        manager.diagnostic(
            message="Test",
            destination=(
                ReportDestination.ALL
            ),
        )
