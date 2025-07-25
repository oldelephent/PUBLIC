import pandas as pd
from pathlib import Path 

base_dir = Path.cwd()
filtered_csv_folder = base_dir / "filterd_data"
filtered_csv_folder.mkdir()
blank = base_dir / filtered_csv_folder / "xls_count.csv"
blank.touch()

for i in Path().glob("*.csv"):
                file_names = i.stem
                file_extension = i.suffix
     
                outname = fr"{base_dir}\filterd_data\{file_names}.csv"

                # Read the data from the file
                df = pd.read_csv(i)

                ##Apply filters to the data
                filtered_data = df[
                    (df['Connection Status'] == "Connected") &
                    (~df['Description'].str.contains("_Web", na=False)) 
                    #(~df['Description'].str.contains("Login Successfull from IP", na=False))
                ]

                # Get unique UserID entries
                unique_codes = filtered_data.drop_duplicates(subset='UserID')

                # Initialize counters for Android and iOS (reset for each file)
                android_users = set()
                ios_users = set()
                ctcl = set()

                # Loop through the filtered data to classify the users
                for _, row in unique_codes.iterrows():
                    user_id = row['UserID']
                    description = row['Description']

                    if description.endswith("Android"):
                        android_users.add(user_id)  # Add to Android if ends with Android
                    elif description.startswith("Login Successfull from IP -"):
                           ctcl.add(user_id)
                    else:
                        ios_users.add(user_id)  # Everything else goes to iOS

                # Count unique user IDs for Android, iOS, and Total
                android_count = len(android_users)
                ios_count = len(ios_users)
                ctcl_count = len(ctcl)
                total_count = android_count + ios_count +ctcl_count

                unique_codes.to_csv(outname , index=False,header=True)
                print("File Processed:- " + file_names)


                data = pd.DataFrame ([{'File_name': file_names,
                                         'Android': android_count, 
                                         'Ios':ios_count, 
                                         'ctcl':ctcl_count,
                                         'Total':total_count}])
                
                write_header = blank.stat().st_size == 0
                data.to_csv(blank,mode='a',index=False,header=write_header )
            