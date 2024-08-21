curl -O "https://www.bseindia.com/downloads/Help/file/scrip.zip"
curl -O "https://www.bseindia.com/downloads/Help/file/CO.zip"
curl -O "https://www.bseindia.com/downloads1/INDEX_CO.zip"
curl -O "https://www.bseindia.com/downloads1/Master.zip"
curl -O "https://www.bseindia.com/downloads1/BFXREF.zip"
curl -O "https://www.bseindia.com/downloads1/Live_Masters_for_Equity_Derivatives.zip"
curl -O "https://www.bseindia.com/downloads1/Master.zip"

timeout /t 5

7z e "BFXREF.zip" -aoa
7z e "CO.zip" -aoa
7z e "INDEX_CO.zip" -aoa
7z e "Live_Masters_for_Equity_Derivatives.zip" -aoa
7z e "Master.zip" -aoa

timeout /t 5
REM EXTRACTING SCRIP DATA

7z e scrip.zip "scrip\BSE_EQ_SCRIP_*" 
7z e scrip.zip "scrip\CI*"
7z e scrip.zip "scrip\CORPACT_*"
7z e scrip.zip "scrip\DEBTINFO_*"
7z e scrip.zip "scrip\DP*" 
7z e scrip.zip "scrip\EQ_PARTICIPANT*" 
7z e scrip.zip "scrip\REG_IND*" 
7z e scrip.zip "scrip\SCRIP_*.txt"
7z e scrip.zip "scrip\SYSBAS_*" 

timeout /t 5
REM DELETING FILES 

del "BFXREF.zip" 
del "CO.zip" 
del "INDEX_CO.zip" 
del "Live_Masters_for_Equity_Derivatives.zip" 
del "Master.zip"
del "scrip.zip"
