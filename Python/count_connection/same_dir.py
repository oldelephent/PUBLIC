# import pandas as pd
# import os 


# xls_file_path = os.getcwd() 

# os.makedirs(fr"{xls_file_path}\filterd_data", exist_ok=True)

# for i in range(100):
#     file_path = fr"{xls_file_path}" + fr"\ConnectionInfo{i}.xls"
#     outname = fr"{xls_file_path}" + fr"\filterd_data\ConnectionInfo{i}.xlsx"

#     if not os.path.exists(file_path):
#         continue

#     # Read the Excel file (it seems to be .xls, not a CSV)
#     df = pd.read_csv(file_path,sep='\t')

#     # Apply filters correctly with parentheses
#     filtered_data = df[
#         (df['Connection Status'] == "Connected") & (
#             (~df['Description'].str.contains("_Web",na=False)) &
#             (~df['Description'].str.contains("Login Successfull from IP",na=False)) 
            
#         )
#     ]

#     # Get unique UserID entries from filtered data
#     unique_codes = filtered_data.drop_duplicates(subset='UserID')
    
#     # Save to Excel
#     unique_codes.to_excel(outname, index=False,header=False)
#     print("File Processed:- " + os.path.basename(file_path))
