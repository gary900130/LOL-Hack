@echo off
if "%1" == "h" goto begin
mshta Vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin
echo hacking...
start "" /B python "guagou.py"
if errorlevel 1 (
    echo error
    pause
) else (
    echo Hacking!!!
)
pause