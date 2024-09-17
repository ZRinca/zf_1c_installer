@echo Этот батник удаляет службу Apache, убивает его процессы, чистит от него реестр, удаляет задачи zf_connector и удаляет папки zf_connector и Apache
@echo.  
@echo Если вы не хотите делать этого, то самое время закрыть батник!
PAUSE
@echo. 

@echo Последний шанс!
PAUSE
@echo. 

@echo Теперь уж точно...
PAUSE
@echo. 

@echo Ну, я вас предупредил...
@echo. 

@echo Удаляю службу Apache
sc delete Apache2.4
@echo. 

@echo Убиваю процессы Apache и ZeroFactor
taskkill /f /im httpd.exe
taskkill /f /im zf_connector.exe
taskkill /f /im zf_setup.exe
@echo. 

@echo Начинаю очистку реестра
Reg delete "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\EventLog\Application\Apache Service" /f
Reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Application\Apache Service" /f
@echo. 

@echo Приступаю к удалению задач
del C:\Windows\System32\Tasks\ZeroFactor\Base_?.* /F /Q
@echo. 

@echo Удаляю папки Apache и ZeroFactor
rmdir "C:\Apache24" /s /q
rmdir "C:\zf_connector" /s /q
@echo. 

@echo Дело сделано

PAUSE