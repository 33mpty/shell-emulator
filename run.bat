@echo off
rem Run the emulator on Windows. All arguments are passed through.
cd /d "%~dp0"
set PYTHONPATH=src
python -m emulator %*
