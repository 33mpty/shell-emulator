#!/bin/sh
# Запуск со всеми параметрами: VFS и стартовый скрипт.
cd "$(dirname "$0")/.." || exit 1
./run.sh --vfs vfs/minimal.xml --script startup/basic.txt < /dev/null
