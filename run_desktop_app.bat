@echo off
setlocal
cd /d "%~dp0"

set "TARGET_HTML=%~dp0demos\wincommerce_desktop_standalone.html"
set "EDGE_PATH=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
set "EDGE_PATH_64=C:\Program Files\Microsoft\Edge\Application\msedge.exe"
set "CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe"

if exist "%EDGE_PATH%" (
    start "" "%EDGE_PATH%" --app="file:///%TARGET_HTML:\=/%" --window-size=1440,900
    exit /b 0
)

if exist "%EDGE_PATH_64%" (
    start "" "%EDGE_PATH_64%" --app="file:///%TARGET_HTML:\=/%" --window-size=1440,900
    exit /b 0
)

if exist "%CHROME_PATH%" (
    start "" "%CHROME_PATH%" --app="file:///%TARGET_HTML:\=/%" --window-size=1440,900
    exit /b 0
)

start "" "%TARGET_HTML%"
exit /b 0
