#!/bin/sh
# Запуск только со стартовым скриптом, в котором есть ошибки.
cd "$(dirname "$0")/.." || exit 1
./run.sh --script startup/errors.txt < /dev/null
