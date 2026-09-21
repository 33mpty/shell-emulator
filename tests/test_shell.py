"""Тесты главного цикла оболочки."""

from emulator.shell import Shell


def test_prompt_contains_vfs_name():
    assert Shell("myvfs").prompt() == "myvfs> "


def test_exit_stops_loop():
    assert Shell("vfs").execute("exit") is False


def test_unknown_command(capsys):
    Shell("vfs").execute("foo bar")
    assert "команда не найдена" in capsys.readouterr().out


def test_stub_prints_name_and_args(capsys):
    Shell("vfs").execute("ls -l /home")
    assert capsys.readouterr().out == "ls -l /home\n"


def test_cd_wrong_args(capsys):
    Shell("vfs").execute("cd a b")
    assert "ожидается один аргумент" in capsys.readouterr().out
