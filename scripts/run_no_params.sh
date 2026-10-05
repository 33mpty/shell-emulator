#!/bin/sh
# Запуск без параметров: имя VFS берётся по умолчанию.
cd "$(dirname "$0")/.." || exit 1
./run.sh < /dev/null
