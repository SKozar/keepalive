"""Syntax checks — no imports, safe on any platform."""

import ast
import pathlib

GUI_DIR = pathlib.Path("src/gui")


def test_app_syntax():
    """gui/app.py has no SyntaxError."""
    ast.parse((GUI_DIR / "app.py").read_text())


def test_settings_syntax():
    """gui/settings_window.py has no SyntaxError."""
    ast.parse((GUI_DIR / "settings_window.py").read_text())


def test_main_syntax():
    """gui/__main__.py has no SyntaxError."""
    ast.parse((GUI_DIR / "__main__.py").read_text())
