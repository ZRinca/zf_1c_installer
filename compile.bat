cmd /U /k "env\Scripts\activate&&pip install pyinstaller&&pyinstaller main.py&&exit"

xcopy /y /e "ico\*.*" "dist\main\_internal\ico\*.*"

xcopy /y /e "Apache\*.*" "dist\main\Apache\*.*"
xcopy /y /e "zf_1c_connect_client\*.*" "dist\main\zf_1c_connect_client\*.*"
xcopy /y /e "extension\*.*" "dist\main\extension\*.*"

copy "PLINK.EXE" "dist\main\PLINK.EXE"

PAUSE