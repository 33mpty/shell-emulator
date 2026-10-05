"""Точка входа: python -m emulator [--vfs PATH] [--script PATH]."""

import sys

from emulator.config import parse_args, print_debug
from emulator.script_runner import ScriptError, run_script
from emulator.shell import Shell

ERROR_EXIT_CODE = 1


def run_startup_script(shell, path):
    """Выполнить стартовый скрипт. Вернуть False, если был exit."""
    try:
        return run_script(shell, path)
    except ScriptError as error:
        sys.stdout.flush()
        print(error, file=sys.stderr)
        return True


def main(argv=None):
    """Разобрать параметры, выполнить скрипт и открыть диалог."""
    config = parse_args(argv)
    print_debug(config)
    shell = Shell(config.vfs_name)
    if config.script_path is not None:
        if not run_startup_script(shell, config.script_path):
            return 0
    shell.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
