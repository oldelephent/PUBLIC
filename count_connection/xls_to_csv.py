
import os
import pandas as pd

# Set the directory containing .xls files
input_folder = r"E:\ABHISHEK\WORKING\python\VISHWAS\counting_unique_user\connectioninfo 1apr to 30 apr"
output_folder = r"E:\ABHISHEK\WORKING\python\VISHWAS\counting_unique_user\csv"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith('.xls'):
        file_path = os.path.join(input_folder, file)
        output_file = os.path.splitext(file)[0] + '.csv'
        output_path = os.path.join(output_folder, output_file)

        try:
            # Try reading it as an Excel file
            df = pd.read_excel(file_path, engine='xlrd')
        except Exception as e:
            # If it fails, try reading it as a tab-separated file
            try:
                df = pd.read_csv(file_path, sep='\t')
                print(f"Read as TSV: {file}")
            except Exception as e2:
                print(f"Failed to read {file}: {e2}")
                continue

        df.to_csv(output_path, index=False)
        print(f"Saved: {output_file}")
