import requests
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

BASE = "https://www.nseindia.com"
API = "https://www.nseindia.com/api/circulars"

today = datetime.today()
yesterday = today - timedelta(days=1)

params = {
    "fromDate": yesterday.strftime("%d-%m-%Y"),
    "toDate": today.strftime("%d-%m-%Y")
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/resources/exchange-communication-circulars"
}

session = requests.Session()

# Get cookies
session.get(BASE, headers=headers)

# Fetch circulars
r = session.get(API, headers=headers, params=params)
r.raise_for_status()

records = r.json()["data"]

df = pd.DataFrame(records)

# Match NSE download exactly
df = df.rename(columns={
    "cirDisplayDate": "DATE",
    "circDepartment": "DEPARTMENT",
    "circDisplayNo": "DOWNLOAD REFERENCE NO.",
    "sub": "SUBJECT",
    "circFilelink": "LINK",
    "circFileSize": "FILE SIZE",
})

df = df[
    [
        "DATE",
        "DEPARTMENT",
        "DOWNLOAD REFERENCE NO.",
        "SUBJECT",
        "LINK",
        "FILE SIZE",
    ]
]

Path("downloads").mkdir(exist_ok=True)

outfile = f"downloads/NSE_Circulars_{today:%Y%m%d}.csv"

df.to_csv(outfile, index=False)

print(f"Saved {len(df)} records to {outfile}")