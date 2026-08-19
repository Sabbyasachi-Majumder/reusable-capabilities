"""
Validates display rendering behavior.
"""

from reporting.utils.display.display_renderer import (
    DisplayRenderer,
)


def test_render_display(
    capsys,
):
    renderer = DisplayRenderer(refresh_interval_seconds=0)

    renderer.render(
        Files="301,415",
        Directories="4,406",
    )

    captured = capsys.readouterr()

    assert "Files: 301,415" in captured.out

    assert "Directories: 4,406" in captured.out


def test_complete_display(
    capsys,
):
    renderer = DisplayRenderer(refresh_interval_seconds=0)

    renderer.complete()

    captured = capsys.readouterr()

    assert "\n" in captured.out
