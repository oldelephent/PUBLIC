start "" curl -O "https://www.bseindia.com/downloads/Help/file/scrip.zip"
start "" curl -O "https://www.bseindia.com/downloads/Help/file/CO.zip"
start "" curl -O "https://www.bseindia.com/downloads1/INDEX_CO.zip"
start "" curl -O "https://www.bseindia.com/downloads1/Master.zip"
start "" curl -O "https://www.bseindia.com/downloads1/BFXREF.zip"
start "" curl -O "https://www.bseindia.com/downloads1/Live_Masters_for_Equity_Derivatives.zip"
start "" curl -O "https://www.bseindia.com/downloads1/Master.zip"
timeout /T 2
start "" 7z e "BFXREF.zip" -aoa
start "" 7z e "CO.zip" -aoa
start "" 7z e "INDEX_CO.zip" -aoa
start "" 7z e "Live_Masters_for_Equity_Derivatives.zip" -aoa
start "" 7z e "Master.zip" -aoa
timeout /T 2
7z e scrip.zip "scrip\BSE_EQ_SCRIP_*" "scrip\CI*" "scrip\CORPACT_*" "scrip\DEBTINFO_*" "scrip\DP*" "scrip\EQ_PARTICIPANT*" "scrip\REG_IND*" "scrip\SCRIP_*.txt" "scrip\SYSBAS_*" 
timeout /T 2
del "BFXREF.zip" "CO.zip" "INDEX_CO.zip" "Live_Masters_for_Equity_Derivatives.zip" "Master.zip" "scrip.zip"
