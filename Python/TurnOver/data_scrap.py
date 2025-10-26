import pandas as pd
from  pathlib import Path

def filter_data():
        
    xlsx_files = Path(r"")
    output_file = 'single.csv'    
    for file in xlsx_files.glob("*.xlsx"):
        file_names = file.stem

        df = pd.read_excel(file,engine='openpyxl')
        file_columns = df.columns.tolist()

        filtered_rows = [
        'Client',
        'Symbol_ScriptID',
        'Mkt_Seg',
        'Order_Type',
        'B_S',
        'Prod_Type',
        'Price',
        'Total_Qty'
        
        ]
        
        if all(col in file_columns for col in filtered_rows):    
            filtered_data = df[filtered_rows]
            with open(output_file, 'a') as f:
                f.write(f"\nFile: {file_names}\n")

            filtered_data.to_csv(output_file,index=False,mode='a')

filter_data()

