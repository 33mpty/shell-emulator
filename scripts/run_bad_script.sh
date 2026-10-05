#!/bin/sh
# Запуск с несуществующим скриптом: проверка сообщения об ошибке.
cd "$(dirname "$0")/.." || exit 1
./run.sh --script startup/нет-такого.txt < /dev/null
