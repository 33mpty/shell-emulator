"""Точка входа: python -m emulator."""

from emulator.shell import Shell

DEFAULT_VFS_NAME = "vfs"


def main():
    """Создать оболочку и запустить её."""
    Shell(DEFAULT_VFS_NAME).run()


if __name__ == "__main__":
    main()
