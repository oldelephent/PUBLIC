$adapter = "Ethernet"
$stats1 = Get-NetAdapterStatistics -Name $adapter
Start-Sleep -Seconds 5
$stats2 = Get-NetAdapterStatistics -Name $adapter

$rx = ($stats2.ReceivedBytes - $stats1.ReceivedBytes) * 8 / 5 / 1MB
$tx = ($stats2.SentBytes - $stats1.SentBytes) * 8 / 5 / 1MB

Write-Host "Average Download: $([math]::Round($rx, 2)) Mbps, Average Upload: $([math]::Round($tx, 2)) Mbps (over 5 seconds)"
