$logFile = "C:\Logs\UnresponsiveProcesses.log"
$unresponsiveTracker = @{}
$explorerRestarted = $false

# Ensure log directory exists
if (!(Test-Path -Path (Split-Path $logFile))) {
    New-Item -ItemType Directory -Path (Split-Path $logFile) -Force | Out-Null
}

while ($true) {
    $now = Get-Date
    $explorerRestarted = $false

    foreach ($proc in Get-Process) {
        $pid = $proc.Id
        $procName = $proc.Name

        if (-not $proc.Responding) {
            if ($unresponsiveTracker.ContainsKey($pid)) {
                $elapsed = $now - $unresponsiveTracker[$pid]
                if ($elapsed.TotalMinutes -ge 1) {
                    try {
                        Stop-Process -Id $pid -Force
                        $logEntry = "$($now.ToString('yyyy-MM-dd HH:mm:ss')) - Killed process '$procName' (PID: $pid) after $([math]::Round($elapsed.TotalSeconds)) seconds unresponsive"
                        Add-Content -Path $logFile -Value $logEntry

                        # Restart explorer if it was killed
                        if ($procName -eq "explorer" -and -not $explorerRestarted) {
                            Start-Process "explorer.exe"
                            Add-Content -Path $logFile -Value "$($now.ToString('yyyy-MM-dd HH:mm:ss')) - Restarted explorer.exe"
                            $explorerRestarted = $true
                        }

                        $unresponsiveTracker.Remove($pid)
                    } catch {
                        $logEntry = "$($now.ToString('yyyy-MM-dd HH:mm:ss')) - FAILED to kill process '$procName' (PID: $pid): $_"
                        Add-Content -Path $logFile -Value $logEntry
                    }
                }
            } else {
                $unresponsiveTracker[$pid] = $now
            }
        } else {
            $unresponsiveTracker.Remove($pid) | Out-Null
        }
    }

    Start-Sleep -Seconds 5
}
