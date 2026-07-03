import requests
import pandas as pd
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)

url = "https://www.nseindia.com/api/circulars"

params = {
    "fromDate": yesterday.strftime("%d-%m-%Y"),
    "toDate": today.strftime("%d-%m-%Y"),
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/resources/exchange-communication-circulars",
}

session = requests.Session()

# Get cookies
session.get("https://www.nseindia.com", headers=headers)

# Get circulars
response = session.get(url, params=params, headers=headers)
response.raise_for_status()

records = response.json().get("data", [])

# Create dataframe
df = pd.DataFrame(records)

# Rename columns to match NSE download
df = df.rename(columns={
    "cirDisplayDate": "DATE",
    "circDepartment": "DEPARTMENT",
    "circDisplayNo": "DOWNLOAD REFERENCE NO.",
    "sub": "SUBJECT",
    "circFilelink": "LINK",
    "circFileSize": "FILE SIZE",
})

# Always create these columns, even if there are no records
columns = [
    "DATE",
    "DEPARTMENT",
    "DOWNLOAD REFERENCE NO.",
    "SUBJECT",
    "LINK",
    "FILE SIZE",
]

df = df.reindex(columns=columns)

filename = f"NSE_Circulars_{today:%Y%m%d}.csv"

df.to_csv(filename, index=False)

print(f"Saved {len(df)} record(s) to {filename}")