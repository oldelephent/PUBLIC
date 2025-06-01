#$all_folders = 'E:\test\test2'

#$paste_folder = 'E:\test\test3'

$files_for_all_folders = Get-ChildItem -Path $all_folders -Recurse -File

foreach ($file in $files_for_all_folders) {
    #$new_name = $file.Name + "_" + $file.CreationTime.ToString("dd-MM-yyyy_HH-mm-ss") + $file.Extension # Use CreationTime for the creation date with time
    #$new_name = $file.Name + "_" + $file.LastWriteTime.ToString("dd-MM-yyyy_HH-mm-ss") + $file.Extension # Use LastWriteTime for the last modified date with time
    #$new_name = $file.Name+"_" + $file.CreationTime.ToString("dd-MM-yyy:") + $file.Extension # Use CreationTime for the creation date
    #$new_name = $file.Name+"_" + $file.LastWriteTime.ToString("dd-MM-yyy") + $file.Extension # Use LastWriteTime for the last modified date
    
    $new_path = Join-Path -Path $paste_folder -ChildPath $new_name
    Copy-Item -Path $file.FullName -Destination $new_path -Force
}   


