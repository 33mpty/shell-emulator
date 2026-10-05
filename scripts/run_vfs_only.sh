#!/bin/sh
# Запуск только с путём к VFS: имя VFS попадает в приглашение.
cd "$(dirname "$0")/.." || exit 1
./run.sh --vfs vfs/minimal.xml < /dev/null
