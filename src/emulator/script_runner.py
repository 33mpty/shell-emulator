"""Выполнение стартового скрипта эмулятора."""

COMMENT_PREFIX = "#"


class ScriptError(Exception):
    """Стартовый скрипт не найден или не читается."""


def read_script(path):
    """Прочитать строки скрипта. Бросает ScriptError при ошибке."""
    try:
        with open(path, encoding="utf-8") as source:
            return source.read().splitlines()
    except OSError as error:
        raise ScriptError(
            f"скрипт не выполнен: {path}: {error.strerror}") from error


def is_skipped(line):
    """Проверить, что строку не нужно выполнять: пустая или комментарий."""
    stripped = line.strip()
    return not stripped or stripped.startswith(COMMENT_PREFIX)


def run_script(shell, path):
    """Выполнить скрипт, имитируя диалог. Вернуть False после exit."""
    for line in read_script(path):
        if is_skipped(line):
            continue
        print(shell.prompt() + line)
        if not shell.execute(line):
            return False
    return True
