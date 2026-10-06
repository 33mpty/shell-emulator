"""Тесты выполнения стартового скрипта."""

import pytest

from emulator.script_runner import ScriptError, run_script
from emulator.shell import Shell


def write_script(tmp_path, text):
    """Создать временный файл скрипта."""
    path = tmp_path / "script.txt"
    path.write_text(text, encoding="utf-8")
    return str(path)


def test_shows_input_and_output(tmp_path, capsys):
    path = write_script(tmp_path, "ls -l\n")
    run_script(Shell("vfs"), path)
    assert capsys.readouterr().out == "vfs> ls -l\nls -l\n"


def test_bad_lines_are_skipped(tmp_path, capsys):
    path = write_script(tmp_path, "privet\ncd a b\nls\n")
    run_script(Shell("vfs"), path)
    out = capsys.readouterr().out
    assert "команда не найдена" in out
    assert "ожидается один аргумент" in out
    assert out.endswith("vfs> ls\nls\n")


def test_comments_and_blank_lines_ignored(tmp_path, capsys):
    path = write_script(tmp_path, "# комментарий\n\nls\n")
    run_script(Shell("vfs"), path)
    assert capsys.readouterr().out == "vfs> ls\nls\n"


def test_exit_stops_script(tmp_path, capsys):
    path = write_script(tmp_path, "ls\nexit\nls\n")
    assert run_script(Shell("vfs"), path) is False
    assert capsys.readouterr().out == "vfs> ls\nls\nvfs> exit\n"


def test_missing_file(tmp_path):
    with pytest.raises(ScriptError):
        run_script(Shell("vfs"), str(tmp_path / "нет.txt"))
