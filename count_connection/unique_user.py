import csv

file_paths = r"E:\ConnectionInfo1.xls"

# android_set = set()
# ios_set = set()

# with open('C_CSV.csv','r')as f1:
# #with open(file_paths,'r')as f1:
#     file_read = csv.DictReader(f1)
#     for i in file_read:
#         if i["Connection Status"] == 'Connected':
#             description = i["Description"].lower()
#             user_id = i["UserID"]

#             if "_android" in description:
#                 android_set.add(user_id)
#             if "ios" in description:
#                 ios_set.add(user_id)
#             if "io" in description:
#                 ios_set.add(user_id)
            
# print("android:-",len( android_set))
# print("ios:-", len( ios_set))

######################################################################################################################################################    XLS

# import pandas as pd
# # Read the file as a tab-separated text file
# df = pd.read_csv(file_paths, sep='\t')

# # Initialize sets to store unique user IDs
# android_set = set()
# ios_set = set()

# # Iterate through rows
# for _, row in df.iterrows():
#     if row["Connection Status"] == 'Connected':
#         description = str(row["Description"]).lower()
#         user_id = row["UserID"]

#         if "_android" in description:
#             android_set.add(user_id)
#         if "ios" in description:
#             ios_set.add(user_id)
#         if "io" in description:
#             ios_set.add(user_id)

# # Output the counts
# print("android:-", len(android_set))
# print("ios:-", len(ios_set))

#_________________________________________________________________________________________________________________________________________________________
# # output total adnroid and ios users 
# import pandas as pd

# # Read the file as a tab-separated text file
# df = pd.read_csv(file_paths, sep='\t')

# # Initialize sets to store unique user IDs
# android_set = set()
# ios_set = set()

# # Iterate through rows
# for _, row in df.iterrows():
#     if row["Connection Status"] == 'Connected':
#         description = str(row["Description"]).lower()
#         user_id = row["UserID"]

#         if "_android" in description:
#             android_set.add(user_id)
#         if "ios" in description or "io" in description:
#             ios_set.add(user_id)

# # Combine both sets into one
# all_user_ids = android_set.union(ios_set)

# # Create a DataFrame with a single column
# output_df = pd.DataFrame({'UserID': list(all_user_ids)})

# # Save to CSV
# output_df.to_csv('userids_single_column.csv', index=False)

# print("Output saved to userids_single_column.csv")

#__________________________________________________________________________________________________________
# #total unique user android + ios 
# import pandas as pd

# # Read the file as a tab-separated text file
# df = pd.read_csv(file_paths, sep='\t')

# # Initialize sets to store unique user IDs
# android_set = set()
# ios_set = set()

# # Iterate through rows
# for _, row in df.iterrows():
#     if row["Connection Status"] == 'Connected':
#         description = str(row["Description"]).lower()
#         user_id = row["UserID"]

#         if "_android" in description:
#             android_set.add(user_id)
#         if "ios" in description or "io" in description:
#             ios_set.add(user_id)

# # Combine sets and print total unique count
# total_unique_users = android_set.union(ios_set)
# print(f"Total unique users (Android + iOS): {len(total_unique_users)}")


#############################################################################################################################################################
# import pandas as pd

# # Load CSV
# #df = pd.read_csv("your_file.csv")
# #df = pd.read_csv("C_CSV.csv")
# df = pd.read_csv("ConnectionInfo.xls")

# # Filter only login (connected) rows
# login_df = df[df['Connection Status'] == 'Connected']

# # Android logins
# android_users = login_df[login_df['Description'].str.contains('_Android', na=False)]['UserID'].unique()

# # iOS logins
# ios_users = login_df[login_df['Description'].str.contains('_IOS', na=False)]['UserID'].unique()

# # Print results
# print("Unique Android users:", len(android_users))
# print("Unique iOS users:", len(ios_users))

############################################################################################################################################################
# import pandas as pd

# # Load XLS
# df = pd.read_excel("ConnectionInfo.xls",engine='xlrd')  # Change the filename if needed

# # Filter only login (connected) rows
# login_df = df[df['Connection Status'] == 'Connected']

# # Android logins
# android_users = login_df[login_df['Description'].str.contains('_Android', na=False)]['UserID'].unique()

# # iOS logins
# ios_users = login_df[login_df['Description'].str.contains('_IOS', na=False)]['UserID'].unique()

# # Print results
# print("Unique Android users:", len(android_users))
#print("Unique iOS users:", len(ios_users))
