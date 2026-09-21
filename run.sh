#!/bin/sh
# Запуск эмулятора. Все аргументы передаются программе.
cd "$(dirname "$0")" && PYTHONPATH=src python3 -m emulator "$@"
