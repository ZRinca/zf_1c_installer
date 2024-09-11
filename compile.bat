cmd /U /k "env\Scripts\activate&&pip install pyinstaller&&pyinstaller --name zf_setup --icon=ico\ZF_green.ico --add-data ico\;ico --version-file=version_info.rc main.py&&exit"

xcopy /y /e "ico\*.*" "dist\zf_setup\ico\"
xcopy /y /e "Apache\*.*" "dist\zf_setup\Apache\*.*"
xcopy /y /e "zf_1c_connect_client\*.*" "dist\zf_setup\zf_1c_connect_client\*.*"
xcopy /y /e "extension\*.*" "dist\zf_setup\extension\*.*"

copy "PLINK.EXE" "dist\zf_setup\PLINK.EXE"
copy "version_info.rc" "dist\zf_setup\version_info.rc"

PAUSE