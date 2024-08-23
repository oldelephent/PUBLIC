start "" powershell.exe invoke-webrequest -uri "https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR230824.zip" -outfile (Split-Path -Path "https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR230824.zip" -leaf)
start "" powershell.exe invoke-webrequest -uri "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20240823_F_0000.csv.zip" -outfile (Split-Path -Path "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20240823_F_0000.csv.zip" -leaf)
start "" powershell.exe invoke-webrequest -uri "https://nsearchives.nseindia.com/content/fo/BhavCopy_NSE_FO_0_0_0_20240823_F_0000.csv.zip" -outfile (Split-Path -Path "https://nsearchives.nseindia.com/content/fo/BhavCopy_NSE_FO_0_0_0_20240823_F_0000.csv.zip" -leaf)
start "" powershell.exe invoke-webrequest -uri "https://nsearchives.nseindia.com/archives/cd/bhav/BhavCopy_NSE_CD_0_0_0_20240823_F_0000.csv.zip" -outfile (Split-Path -Path "https://nsearchives.nseindia.com/archives/cd/bhav/BhavCopy_NSE_CD_0_0_0_20240823_F_0000.csv.zip" -leaf)

timeout /t 10 

7z e BhavCopy_NSE_CD_0_0_0_*
7z e BhavCopy_NSE_CM_0_0_0_*
7z e BhavCopy_NSE_FO_0_0_0_*
7z e PR230824.zip Pd*

timeout /t 10 

move BhavCopy_NSE_CD_0_0_0_*.csv b
move BhavCopy_NSE_CM_0_0_0_*.csv b
move BhavCopy_NSE_FO_0_0_0_*.csv b
move pd*.csv b


timeout /t 10 

start "" curl -O "https://www.bseindia.com/downloads/Help/file/scrip.zip"
start "" curl -O "https://www.bseindia.com/downloads/Help/file/CO.zip"
start "" curl -O "https://www.bseindia.com/downloads1/INDEX_CO.zip"
start "" curl -O "https://www.bseindia.com/downloads1/Master.zip"
start "" curl -O "https://www.bseindia.com/downloads1/BFXREF.zip"
start "" curl -O "https://www.bseindia.com/downloads1/Live_Masters_for_Equity_Derivatives.zip"
start "" curl -O "https://www.bseindia.com/downloads1/Master.zip"

timeout /T 10

start "" 7z e "BFXREF.zip" -aoa
start "" 7z e "CO.zip" -aoa
start "" 7z e "INDEX_CO.zip" -aoa
start "" 7z e "Live_Masters_for_Equity_Derivatives.zip" -aoa
start "" 7z e "Master.zip" -aoa
timeout /T 2
7z e scrip.zip "scrip\BSE_EQ_SCRIP_*" "scrip\CI*" "scrip\CORPACT_*" "scrip\DEBTINFO_*" "scrip\DP*" "scrip\EQ_PARTICIPANT*" "scrip\REG_IND*" "scrip\SCRIP_*.txt" "scrip\SYSBAS_*" 

timeout /T 2

del "BFXREF.zip" "CO.zip" "INDEX_CO.zip" "Live_Masters_for_Equity_Derivatives.zip" "Master.zip" "scrip.zip" "BhavCopy_NSE_CD_0_0_0_*" "BhavCopy_NSE_CM_0_0_0_*" "BhavCopy_NSE_FO_0_0_0_*" "PR*"

