@echo off
timeout /t 10 > nul
echo BAT started at %date% %time% >> C:\temp\bat_log.txt

python "C:/Users/Sanjay Singh/Documents/startup_apps/powerping/app.py" >> C:\temp\python_output.txt 2>&1