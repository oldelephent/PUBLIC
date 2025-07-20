import os
import pandas as pd

#current dir for xls
csv_file_path = os.getcwd() 
    
# #making filterd_data folder in same dir for filtered xls
os.makedirs(fr"{csv_file_path}\filterd_data", exist_ok=True)

# # Define the file paths for filtered csv 
blank = fr"{csv_file_path}\csv_count.csv"

for i in os.listdir(csv_file_path):
        if i.endswith('.csv'):
                
                #Extract the file name without extension
                file_name = os.path.splitext(i)[0]

                outname = fr"{csv_file_path}\filterd_data\{file_name}.csv"
                
                # Read the data from the file
                df = pd.read_csv(i)

                # Apply filters to the data
                filtered_data = df[
                    (df['Connection Status'] == "Connected") & 
                    (~df['Description'].str.contains("_Web", na=False)) &
                    (~df['Description'].str.contains("Login Successfull from IP", na=False))
                ]

                # Get unique UserID entries
                unique_codes = filtered_data.drop_duplicates(subset='UserID')

                # Initialize counters for Android and iOS (reset for each file)
                android_users = set()
                ios_users = set()

                # Loop through the filtered data to classify the users
                for _, row in unique_codes.iterrows():
                    user_id = row['UserID']
                    description = row['Description']
                    
                    if description.endswith("Android"):
                        android_users.add(user_id)  # Add to Android if ends with Android
                    else:
                        ios_users.add(user_id)  # Everything else goes to iOS

                # Count unique user IDs for Android, iOS, and Total
                android_count = len(android_users)
                ios_count = len(ios_users)
                total_count = android_count + ios_count

                unique_codes.to_csv(outname , index=False,header=False)
                print("File Processed:- " + os.path.basename(i))

                # Write results to the output file with Total column
                with open(blank, 'a') as f:
                    f.write(f"{os.path.basename(i)}, Android ,{android_count}, iOS, {ios_count}, Total, {total_count}\n")

# os.startfile('xls_count.csv')
# os.startfile('filterd_data')
