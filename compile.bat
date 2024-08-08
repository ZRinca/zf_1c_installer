cmd /U /k "env\Scripts\activate&&pip install pyinstaller&&pyinstaller --name zf_setup --icon=ico\ZF_green.ico main.py&&exit"

xcopy /y /e "ico\*.*" "dist\zf_setup\_internal\ico\*.*"
xcopy /y /e "Apache\*.*" "dist\zf_setup\Apache\*.*"
xcopy /y /e "zf_1c_connect_client\*.*" "dist\zf_setup\zf_1c_connect_client\*.*"
xcopy /y /e "extension\*.*" "dist\zf_setup\extension\*.*"

copy "PLINK.EXE" "dist\zf_setup\PLINK.EXE"

PAUSE