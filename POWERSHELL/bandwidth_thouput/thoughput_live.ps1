$adapter = "Ethernet"  # Change this if needed

while ($true) {
    $stats1 = Get-NetAdapterStatistics -Name $adapter
    Start-Sleep -Seconds 1
    $stats2 = Get-NetAdapterStatistics -Name $adapter

    $rxBytes = ($stats2.ReceivedBytes - $stats1.ReceivedBytes) / 1MB
    $txBytes = ($stats2.SentBytes - $stats1.SentBytes) / 1MB

    Write-Host "Download: $([math]::Round($rxBytes * 8, 2)) Mbps, Upload: $([math]::Round($txBytes * 8, 2)) Mbps"
}



