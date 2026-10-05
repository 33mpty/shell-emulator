#!/bin/sh
# Запуск скрипта с командой exit: диалог не открывается.
cd "$(dirname "$0")/.." || exit 1
./run.sh --vfs vfs/minimal.xml --script startup/with_exit.txt
