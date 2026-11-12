@echo off
chcp 65001 >nul
cd /d "%~dp0Mulakat-Hazirlik"

where python >nul 2>&1
if errorlevel 1 (
  echo Python bulunamadi. python.org uzerinden Python kurup tekrar deneyin.
  pause
  exit /b 1
)

netstat -ano | findstr /C:":8765" | findstr /C:"LISTENING" >nul
if errorlevel 1 (
  start "Mulakat-Notlari" /MIN python -m http.server 8765 --bind 0.0.0.0
  ping 127.0.0.1 -n 2 >nul
)

set "WIFI="
for /f %%I in ('python -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0]); s.close()"') do set "WIFI=%%I"

echo.
echo Bu bilgisayar:
echo   http://127.0.0.1:8765/goruntule.html
echo.
if defined WIFI (
  echo Ayni Wi-Fi uzerinden telefon veya baska bilgisayar:
  echo   http://%WIFI%:8765/goruntule.html
) else (
  echo Wi-Fi adresi alinamadi. Telefonun bu bilgisayarla ayni agda oldugundan emin ol.
)
echo.
echo Test sayfasi: adresin sonuna test.html yaz.
echo.

start "" "http://127.0.0.1:8765/goruntule.html"
pause
