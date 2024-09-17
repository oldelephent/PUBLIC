

$date = 29

invoke-webrequest -uri "https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR${date}0824.zip" -outfile a.zip
invoke-webrequest -uri "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_202408${date}_F_0000.csv.zip" -outfile  b.zip
invoke-webrequest -uri "https://nsearchives.nseindia.com/content/fo/BhavCopy_NSE_FO_0_0_0_202408${date}_F_0000.csv.zip" -outfile c.zip
invoke-webrequest -uri "https://nsearchives.nseindia.com/archives/cd/bhav/BhavCopy_NSE_CD_0_0_0_202408${date}_F_0000.csv.zip" -outfile d.zip
 

