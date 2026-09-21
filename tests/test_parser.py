"""Тесты разбора строки ввода."""

from emulator.parser import parse_line


def test_command_with_args():
    assert parse_line("ls -l /home") == ("ls", ["-l", "/home"])


def test_empty_line():
    assert parse_line("   ") == (None, [])


def test_extra_spaces_ignored():
    assert parse_line("  cd   docs ") == ("cd", ["docs"])
