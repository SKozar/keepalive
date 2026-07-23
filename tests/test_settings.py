"""Settings window tests — macOS only (needs AppKit)."""

import sys

import pytest


@pytest.mark.skipif(sys.platform != "darwin", reason="needs pyobjc/AppKit")
class TestSettingsWindow:
    def test_init_stores_settings(self):
        """SettingsWindow.__init__ stores settings dict."""
        from gui.settings_window import SettingsWindow

        defaults = {
            "method": "mouse",
            "key": "f13",
            "idle": 180,
            "schedule_from": "08:00",
            "schedule_to": "17:00",
        }
        sw = SettingsWindow(defaults)
        assert sw.settings["method"] == "mouse"
        assert sw.settings["key"] == "f13"
        assert sw.settings["idle"] == 180

    def test_fields_dict_created(self):
        """SettingsWindow creates empty fields dict."""
        from gui.settings_window import SettingsWindow

        sw = SettingsWindow(
            {
                "method": "both",
                "key": "f15",
                "idle": 300,
                "schedule_from": "09:00",
                "schedule_to": "18:00",
            }
        )
        assert isinstance(sw.fields, dict)
        assert len(sw.fields) == 0  # empty until show() is called
