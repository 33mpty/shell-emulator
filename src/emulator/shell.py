"""Главный цикл эмулятора: читает ввод, выполняет команды."""

from emulator.commands import COMMANDS, CommandError
from emulator.parser import parse_line

EXIT_COMMAND = "exit"


class Shell:
    """Командная оболочка, привязанная к виртуальной файловой системе."""

    def __init__(self, vfs_name):
        """Создать оболочку с заданным именем VFS."""
        self.vfs_name = vfs_name

    def prompt(self):
        """Вернуть текст приглашения к вводу."""
        return f"{self.vfs_name}> "

    def execute(self, line):
        """Выполнить одну строку. Вернуть False, если пора выходить."""
        command, args = parse_line(line)
        if command is None:
            return True
        if command == EXIT_COMMAND:
            return False
        handler = COMMANDS.get(command)
        if handler is None:
            print(f"{command}: команда не найдена")
            return True
        try:
            handler(args)
        except CommandError as error:
            print(error)
        return True

    def run(self):
        """Запустить интерактивный цикл до команды exit или конца ввода."""
        while True:
            try:
                line = input(self.prompt())
            except EOFError:
                print()
                break
            if not self.execute(line):
                break
