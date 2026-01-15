import pandas as pd
from pathlib import Path
import json
import requests

with open("api.txt",'r')as f:
    api_token = f.read()

json_folder = Path.cwd() / "json_folder" 
json_folder.mkdir(parents=True, exist_ok=True)

csv_folder = Path.cwd() / "csv"
csv_folder.mkdir(parents=True,exist_ok=True)

industries = [
    "Basic Materials",
    "Communication Services",
    "Consumer Cyclical",
    "Consumer Defensive",
    "Consumer Goods",
    "Energy",
    "Financial",
    "Financial Services",
    "Healthcare",
    "Industrial Goods",
    "Industrials",
    "Real Estate",
    "Services",
    "Technology",
    "Utilities"
]


def json_csv(json_file):
    json_path_file = Path(json_file)

    with open(json_path_file,'r',encoding="utf-8") as f:
        read_json_data = json.load(f)
        df = pd.DataFrame(read_json_data['data'])
        file_name = json_path_file.stem

        required_cols = ["title", "description", "url", "image_url"]

        missing_cols = set(required_cols) - set(df.columns)

        if missing_cols:
            return

        df = df[required_cols]
        print(f"Processing this file {file_name}")
        df.to_csv(csv_folder / f"{file_name}.csv",index=False)


def download_json(industries,json_folder):    
    base_url = "https://api.marketaux.com/v1/news/all"

    for i in industries:

        params = {
            "api_token":f"{api_token}",
            "industries":f"{i}",
            "countries":"in"
        }
        
        response = requests.get(base_url,params=params).json()
        
        with open(json_folder  / f"{i}.json", "w", encoding="utf-8") as f:
            json.dump(response, f, indent=4, ensure_ascii=False)
            json_file = json_folder / f"{i}.json"
            print(json_file)                                   
        json_csv(json_file)
            
download_json(industries,json_folder)
