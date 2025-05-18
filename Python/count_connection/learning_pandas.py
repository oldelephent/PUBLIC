# import pandas as pd
# import os 


# for i in range(31):
#     file_path = fr"E:\counting_unique_user\xls\ConnectionInfo{i}.xls"
#     outname = fr'E:\counting_unique_user\out\ConnectionInfo{i}.xlsx'
#     #outname = fr'E:\counting_unique_user\out\out{i}.xlsx'

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


##### reading excel file and filtering data #####

# for i in range(31):
#     file_path = fr"E:\counting_unique_user\connectioninfo 1apr to 30 apr\ConnectionInfo{i}.xls"
#     outname = fr'E:\counting_unique_user\out\out{i}.csv'

    # if not os.path.exists(file_path):
    #     continue

    # # Read the Excel file (it seems to be .xls, not a CSV)
    # df = pd.read_csv(file_path,sep='\t')

    # # Apply filters correctly with parentheses
    # filtered_data = df[
    #     (df['Connection Status'] == "Connected") & (
    #         df['Description'].str.contains("_Android", na=False) |
    #         df['Description'].str.contains("_IOS", na=False) |
    #         df['Description'].str.contains("_I", na=False)
    #     )
    # ]

    # # Get unique UserID entries from filtered data
    # unique_codes = filtered_data.drop_duplicates(subset='UserID')

    # # Save to Excel
    # unique_codes.to_csv(outname, index=False)

#__________________________________________________________________________________________________________________________________________________________________

# import pandas as pd
# import os 

# android_set = set()
# ios_set = set()

# blank_txt = r"E:\counting_unique_user\xls_count.txt" # CSV OR TXT
# xls_folder_path = r"E:\counting_unique_user\xls"

# for i in range(10000):
#     file_path = xls_folder_path + fr"\ConnectionInfo{i}.xls"
#     outname = fr"E:\counting_unique_user\out\connectioninfo{i}.xlsx"
#     if not os.path.exists(file_path):
#         continue
    
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

#     data = unique_codes['UserID'].count()

#     with open(blank_txt, 'a') as f:
#         f.write((os.path.basename(file_path) + "," +str(data)) +"\n")  

#___________________________________________________________________________________________________________________________________________________________________________________________
#2ND VERSION
# import pandas as pd
# import os 
# import csv

# blank_txt = r"E:\counting_unique_user\xls_count.csv" # CSV OR TXT
# xls_folder_path = r"E:\counting_unique_user\xls"

# for i in range(10000):
#     file_path = xls_folder_path + fr"\ConnectionInfo{i}.xls"
#     outname = fr"E:\counting_unique_user\out\connectioninfo{i}.xlsx"
#     if not os.path.exists(file_path):
#         continue
    
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

#     android_set = set()
#     ios_set = set()
    
#     for _, row in unique_codes.iterrows():
#         user_id = row['UserID']
#         description = row['Description']
        
#         if description.endswith("_Android"):
#             android_set.add(user_id)
#         else:  
#             ios_set.add(user_id)

#     android_count = len(android_set)
#     ios_count = len(ios_set)
#     total_count = android_count + ios_count
        
#     with open(blank_txt, 'a',newline='') as f:
#         writer = csv.writer(f)
#         header = ['File Name', 'Android Count', 'iOS Count', 'Total Count']
#         writer.writerow(header)
#         writer.writerow([os.path.basename(file_path), android_count, ios_count, total_count])
       
      

#__________________________________________________________________________________________________________________________________________________________________________________________
# 3RD VERSION


# import os
# import pandas as pd

# # Define the file paths
# blank = r"E:\counting_unique_user\xls_count.csv"
# xls_folder_path = r"E:\counting_unique_user\xls"

# # Loop through the files and process each one
# for i in range(10000):
#     file_path = xls_folder_path + fr"\ConnectionInfo{i}.xls"
#     outname = fr"E:\counting_unique_user\out\connectioninfo{i}.xlsx"
    
#     # Skip files that don't exist
#     if not os.path.exists(file_path):
#         continue
    
#     # Read the data from the file
#     df = pd.read_csv(file_path, sep='\t')
    
#     # Apply filters to the data
#     filtered_data = df[
#         (df['Connection Status'] == "Connected") & 
#         (~df['Description'].str.contains("_Web", na=False)) &
#         (~df['Description'].str.contains("Login Successfull from IP", na=False))
#     ]
    
#     # Get unique UserID entries
#     unique_codes = filtered_data.drop_duplicates(subset='UserID')
    
#     # Initialize counters for Android and iOS (reset for each file)
#     android_users = set()
#     ios_users = set()
    
#     # Loop through the filtered data to classify the users
#     for _, row in unique_codes.iterrows():
#         user_id = row['UserID']
#         description = row['Description']
        
#         if description.endswith("Android"):
#             android_users.add(user_id)  # Add to Android if ends with Android
#         else:
#             ios_users.add(user_id)  # Everything else goes to iOS
    
#     # Count unique user IDs for Android, iOS, and Total
#     android_count = len(android_users)
#     ios_count = len(ios_users)
#     total_count = android_count + ios_count
    
#     # Write results to the output file with Total column
#     with open(blank, 'a') as f:
#         f.write(f"{os.path.basename(file_path)}, Android ,{android_count}, iOS, {ios_count}, Total, {total_count}\n")
    
#     # Optional: Print the counts for this file
#     print(f"File: {os.path.basename(file_path)}")
#     print(f"Android: {android_count}, iOS: {ios_count}, Total: {total_count}\n")
