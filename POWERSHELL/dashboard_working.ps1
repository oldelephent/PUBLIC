
$Files = @(
    "ael_",
    "ael_NIFTY_Options.csv",
    "BFX_CC_CO",
    "BFX_CO",
    "BFX_DP",
    "BFX_PARTICIPANT",
    "BFX_REF",
    "BFX_SPD_CO",
    "BSE_BFX_CONTRACT_",
    "BSE_BFX_SPDCONTRACT_",
    "BSE_EQ_SCRIP_",
    "BSE_EQD_CONTRACT_",
    "BSE_EQD_SPDCONTRACT_",
    "C_VAR1_",
    "cd_contract.txt",
    "cd_participant.txt",
    "cd_spd_contract.txt",
    "ci",
    "CI",
    "contract",
    "CORPACT_",
    "CP",
    "DailyMargin_",
    "DEBTINFO_",
    "DP",
    "EQ_MAP_CC_",
    "EQ_PARTICIPANT",
    "EQ_SET_PRICE_",
    "EQD_CC_CO",
    "EQD_CO",
    "EQD_DP",
    "EQD_INDEX_CO",
    "EQD_PARTICIPANT",
    "EQD_SET_PRICE_",
    "EQD_SPD_CO",
    "F_AEL_OTM_CONTRACTS_",
    "fo_participant.txt",
    "fo_secban.csv",
    "FreeFloat.txt",
    "MCX_PART.bcp",
    "MCXRPF-",
    "MCXScrips.bcp",
    "MS_",
    "nnf_participant.dat",
    "nnf_security.dat",
    "nsccl_x",
    "nsccl.",
    "participant.txt",
    "REG_IND",
    "SCRIP_",
    "SCRIP_CC_",
    "security.txt",
    "spd_contract.txt",
    "SYSBAS_"
)

$folderPath =    "" ## Set Folder Path 

function Show-Dashboard {
    Clear-Host
    Write-Host "==== File Monitoring Dashboard ====" -ForegroundColor Cyan
    Write-Host "Checking folder: $folderPath`n"

    foreach ($pattern in $Files) {
        $matchedFiles = Get-ChildItem -Path $folderPath -File -Name | Where-Object { $_ -like "*$pattern*" }

        if ($matchedFiles.Count -gt 0) {
            Write-Host "$pattern found" -ForegroundColor Green
        } else {
            Write-Host "$pattern missing" -ForegroundColor Red
        }
    }

    Write-Host "`n(Refreshing every 5 seconds...)" -ForegroundColor Yellow
}

while ($true) {
    Show-Dashboard
    Start-Sleep -Seconds 5
}

