"""Параметры командной строки эмулятора."""

import argparse
import os

DEFAULT_VFS_NAME = "vfs"
PROGRAM_NAME = "emulator"


class Config:
    """Набор параметров запуска эмулятора."""

    def __init__(self, vfs_path=None, script_path=None):
        """Сохранить пути к VFS и стартовому скрипту."""
        self.vfs_path = vfs_path
        self.script_path = script_path

    @property
    def vfs_name(self):
        """Имя VFS для приглашения: берётся из имени файла."""
        if self.vfs_path is None:
            return DEFAULT_VFS_NAME
        name = os.path.basename(self.vfs_path)
        return os.path.splitext(name)[0] or DEFAULT_VFS_NAME


def parse_args(argv=None):
    """Разобрать аргументы командной строки и вернуть Config."""
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description="Эмулятор командной оболочки поверх VFS.")
    parser.add_argument("--vfs", dest="vfs_path", metavar="PATH",
                        help="путь к физическому расположению VFS")
    parser.add_argument("--script", dest="script_path", metavar="PATH",
                        help="путь к стартовому скрипту эмулятора")
    args = parser.parse_args(argv)
    return Config(args.vfs_path, args.script_path)


def format_debug(config):
    """Собрать строки отладочного вывода параметров запуска."""
    return [
        "[debug] параметры запуска:",
        f"[debug]   vfs    = {config.vfs_path or '<не задан>'}",
        f"[debug]   script = {config.script_path or '<не задан>'}",
        f"[debug]   имя VFS в приглашении = {config.vfs_name}",
    ]


def print_debug(config):
    """Напечатать отладочный вывод всех заданных параметров."""
    for line in format_debug(config):
        print(line)
