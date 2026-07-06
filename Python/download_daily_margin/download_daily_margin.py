import csv
import re
from datetime import datetime

import requests


def get_daily_margin(date_str=None):
    """
    Download MCX Daily Margin CSV.

    date_str format: DD/MM/YYYY
    Example: 06/07/2026
    """

    if date_str is None:
        date_str = datetime.now().strftime("%d/%m/%Y")

    session = requests.Session()

    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.mcxccl.com/",
        "Origin": "https://www.mcxccl.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua": '"Google Chrome";v="138", "Chromium";v="138", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    })

    params = {
        "fromDate": date_str,
        "_": int(datetime.now().timestamp() * 1000)
    }

    print(f"Downloading Daily Margin for {date_str}...")

    response = session.get(
        "https://www.mcxccl.com/DailyMargin/GetDailyMargin",
        params=params,
        timeout=30
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    result = response.json()

    if not result.get("IsSuccess"):
        raise Exception(result.get("Message", "API returned an error."))

    data = result.get("Data", [])

    if not data:
        print("No data found.")
        return

    filename = f"DailyMargin_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Date",
            "FileID",
            "InstrumentID",
            "Symbol",
            "Expiry Date",
            "Initial Margin(%)",
            "Tender Margin(%)",
            "Total Margin(%)",
            "Additional Long Margin(%)",
            "Additional Short Margin(%)",
            "Special Long Margin(%)",
            "Special Short Margin(%)",
            "ELM Long (%)",
            "ELM Short (%)",
            "Delivery Margin(%)",
            "Daily Volatility",
            "Annualized Volatility"
        ])

        for row in data:
            ms = int(re.search(r"\d+", row["date"]).group())
            dt = datetime.fromtimestamp(ms / 1000)

            writer.writerow([
                dt.strftime("%d-%m-%Y %H:%M"),
                row["fileID"],
                row["instrumentID"],
                row["symbol"],
                row["expiryDate"],
                row["initialMargin"],
                row["tenderMargin"],
                row["totalMargin"],
                row["additionalLongMargin"],
                row["additionalShortMargin"],
                row["specialLongMargin"],
                row["specialShortMargin"],
                row["elmLong"],
                row["elmShort"],
                row["deliveryMargin"],
                row["dailyVolatility"],
                row["annualizedVolatility"],
            ])

    print(f"Downloaded successfully: {filename}")


if __name__ == "__main__":
    get_daily_margin()