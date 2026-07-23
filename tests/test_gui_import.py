"""GUI import tests — macOS only (needs pyobjc/rumps)."""

import sys

import pytest


@pytest.mark.skipif(sys.platform != "darwin", reason="needs pyobjc/rumps")
def test_gui_app_import():
    """KeepaliveApp imports without error."""
    from gui.app import KeepaliveApp

    assert KeepaliveApp is not None


@pytest.mark.skipif(sys.platform != "darwin", reason="needs pyobjc/AppKit")
def test_gui_settings_import():
    """SettingsWindow imports without error."""
    from gui.settings_window import SettingsWindow

    assert SettingsWindow is not None
