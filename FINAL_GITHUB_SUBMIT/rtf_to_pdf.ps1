$rtf_folder = Read-Host "Enter rtf save folder path" | ForEach-Object { $_.Replace('"','') }
$pdf_save_Dir = Read-Host "Enter pdf save folder" | ForEach-Object { $_.Replace('"','') }

$files = Get-ChildItem $rtf_folder -Filter *.rtf
$word = New-Object -ComObject Word.Application
$word.Visible = $false


foreach ($file in $files) {
    $doc = $word.Documents.Open($file.FullName)
    $pdfPath = "$($pdf_save_Dir)\$($file.BaseName).pdf"
    $doc.SaveAs([ref] $pdfPath, [ref] 17)  # 17 is the constant for PDF format
    $doc.Close()
}
$word.Quit()
