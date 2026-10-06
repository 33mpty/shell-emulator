"""Команды эмулятора. Пока это заглушки: печатают своё имя и аргументы."""


CD_ARGUMENT_COUNT = 1


class CommandError(Exception):
    """Ошибка выполнения команды (неверные аргументы и т.п.)."""


def cmd_ls(args):
    """Заглушка команды ls."""
    print("ls", *args)


def cmd_cd(args):
    """Заглушка команды cd. Принимает ровно один аргумент."""
    if len(args) != CD_ARGUMENT_COUNT:
        raise CommandError("cd: ожидается один аргумент")
    print("cd", *args)


COMMANDS = {
    "ls": cmd_ls,
    "cd": cmd_cd,
}
