"""Тесты разбора параметров командной строки."""

from emulator.config import Config, format_debug, parse_args


def test_no_arguments():
    config = parse_args([])
    assert config.vfs_path is None
    assert config.script_path is None
    assert config.vfs_name == "vfs"


def test_both_arguments():
    config = parse_args(["--vfs", "vfs/minimal.xml",
                         "--script", "startup/basic.txt"])
    assert config.vfs_path == "vfs/minimal.xml"
    assert config.script_path == "startup/basic.txt"


def test_vfs_name_from_path():
    assert Config("vfs/deep_tree.xml").vfs_name == "deep_tree"


def test_debug_output_lists_all_parameters():
    lines = format_debug(parse_args(["--vfs", "a.xml"]))
    joined = "\n".join(lines)
    assert "a.xml" in joined
    assert "<не задан>" in joined
