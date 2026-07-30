# ==============================
# Hardware Inventory Collector
# ==============================

# Network share settings
$SharePath = "\\192.168.0.100\data"
$ShareUser = "viss"
$SharePass = "123"

# Create credential
$SecurePass = ConvertTo-SecureString $SharePass -AsPlainText -Force
$Credential = New-Object System.Management.Automation.PSCredential(
    $ShareUser,
    $SecurePass
)

# Computer information
$Computer = Get-CimInstance Win32_ComputerSystem
$CPU = Get-CimInstance Win32_Processor
$RAM = Get-CimInstance Win32_PhysicalMemory
$OS = Get-CimInstance Win32_OperatingSystem
$Disks = Get-PhysicalDisk

# RAM type conversion
$RAMType = switch ($RAM[0].SMBIOSMemoryType) {
    20 {"DDR"}
    21 {"DDR2"}
    24 {"DDR3"}
    26 {"DDR4"}
    34 {"DDR5"}
    default {"Unknown"}
}

# Build report
$Report = [PSCustomObject]@{

    ComputerName = $env:COMPUTERNAME

    User = $env:USERNAME

    CPU = $CPU.Name

    RAM = @{
        TotalGB = [math]::Round(
            ($RAM | Measure-Object Capacity -Sum).Sum / 1GB,
            2
        )
        Type = $RAMType
        SpeedMHz = $RAM[0].Speed
    }

    Storage = $Disks | ForEach-Object {
        [PSCustomObject]@{
            Name = $_.FriendlyName
            Type = $_.MediaType
            SizeGB = [math]::Round($_.Size / 1GB,2)
        }
    }

    Windows = @{
        Version = $OS.Caption
        Build = $OS.BuildNumber
    }

    Date = Get-Date
}


# Save locally
$FileName = "$env:COMPUTERNAME.json"
$LocalFile = "$env:TEMP\$FileName"

$Report | ConvertTo-Json -Depth 5 | 
    Out-File $LocalFile -Encoding UTF8


# Connect to share
New-PSDrive `
    -Name "INV" `
    -PSProvider FileSystem `
    -Root $SharePath `
    -Credential $Credential `
    -ErrorAction SilentlyContinue


# Copy report
Copy-Item `
    $LocalFile `
    "INV:\$FileName" `
    -Force


# Cleanup
Remove-PSDrive INV


Write-Host "Inventory uploaded:"
Write-Host "$SharePath\$FileName"
