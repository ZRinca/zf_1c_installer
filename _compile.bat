SET activator=env\Scripts\activate
SET installer=pip install pyinstaller pillow

SET comand=pyinstaller
SET comand=%comand% --name zf_setup
SET comand=%comand% --icon=ico\ZF_green.ico
SET comand=%comand% --add-data ico\;ico
SET comand=%comand% --add-data zf_1c_connect_client\;zf_1c_connect_client
SET comand=%comand% --add-data Apache\;Apache/Apache
SET comand=%comand% --add-data extension\;extension
SET comand=%comand% --add-data PLINK.EXE;.
SET comand=%comand% --add-data version_info.rc;.
SET comand=%comand% --onefile
SET comand=%comand% --runtime-tmpdir ./
SET comand=%comand% --splash splash.png
SET comand=%comand% main.py
:: SET comand=%comand% logic/app_starter.py

cmd /U /k "%activator%&&%installer%&&%comand%&&exit"

PAUSE