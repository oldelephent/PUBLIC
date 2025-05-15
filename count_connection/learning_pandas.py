import pandas as pd
import os 

for i in range(31):
    file_path = fr"E:\connectioninfo 1apr to 30 apr\ConnectionInfo{i}.xls"
    outname = fr'E:\counting_unique_user\out\out{i}.xlsx'

    if not os.path.exists(file_path):
        continue

    # Read the Excel file (it seems to be .xls, not a CSV)
    df = pd.read_csv(file_path,sep='\t')

    # Apply filters correctly with parentheses
    filtered_data = df[
        (df['Connection Status'] == "Connected") & (
            (~df['Description'].str.contains("_Web",na=False)) &
            (~df['Description'].str.contains("Login Successfull from IP",na=False)) 
            
        )
    ]

    # Get unique UserID entries from filtered data
    unique_codes = filtered_data.drop_duplicates(subset='UserID')

    # Save to Excel
    unique_codes.to_excel(outname, index=False)





##### reading excel file and filtering data #####

# for i in range(31):
#     file_path = fr"E:\connectioninfo 1apr to 30 apr\ConnectionInfo{i}.xls"
#     outname = fr'E:\counting_unique_user\out\out{i}.xlsx'

#     if not os.path.exists(file_path):
#         continue

#     # Read the Excel file (it seems to be .xls, not a CSV)
#     df = pd.read_csv(file_path,sep='\t')

#     # Apply filters correctly with parentheses
#     filtered_data = df[
#         (df['Connection Status'] == "Connected") & (
#             df['Description'].str.contains("_Android", na=False) |
#             df['Description'].str.contains("_IOS", na=False) |
#             df['Description'].str.contains("_I", na=False)
#         )
#     ]

#     # Get unique UserID entries from filtered data
#     unique_codes = filtered_data.drop_duplicates(subset='UserID')

#     # Save to Excel
#     unique_codes.to_excel(outname, index=False)


