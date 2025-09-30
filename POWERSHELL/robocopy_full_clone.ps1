$tiemstamp = (get-date).ToString("dd-MM-yyy_HH-mm-ss")
$destination = "C:\backup_test\"
mkdir $destination\$tiemstamp
timeout /T 5
$source  = "c:\Users\a\Desktop"
$destinationn = "C:\backup_test\$tiemstamp\"
robocopy "$source" "$destinationn" /E /COPYALL /DCOPY:T /MT:32 /LOG:"$destinationn\copylog.txt"


