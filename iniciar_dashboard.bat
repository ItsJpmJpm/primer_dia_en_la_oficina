@echo off
echo Iniciando servidor web...
echo.
echo Dashboard disponible en: http://localhost:8000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
python -m http.server 8000 --directory .
pause
