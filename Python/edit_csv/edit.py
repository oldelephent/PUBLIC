import csv
import re
#import glob

##SINGLE CODE DIRECT WRITE WITHOUT CREATING LIST
# with open("DP_1.csv", 'r') as dp:
#      file = csv.DictReader(dp)
#      header = file.fieldnames
     
#      with open ("data.csv", 'w',newline='') as dc:
#         writer = csv.DictWriter(dc,fieldnames=header)
#         writer.writeheader()
      
#         for row in file:
#             if row['Client'] == "DCM222":
#                row["Open Authorize Quantity"] = 0
#             writer.writerow(row)

## UPDATA FOR ALL CODE STARTING WBF
# with open("DP_1.csv", 'r') as dp:
#      file = csv.DictReader(dp)
#      header = file.fieldnames
#      data = []

#      for row in file:
#          if re.match("^WBF",row['Client']):
#             row["Open Authorize Quantity"] = 0
#          data.append(row)
 
# with open("DP_1.csv",'w', newline='')as dc:
#    write = csv.DictWriter(dc, fieldnames=header)
#    write.writeheader()
#    write.writerows(data)       


##UPDATE FOR MULTIPLE CODE
# with open("DP_1.csv", 'r') as dp:
#      file = csv.DictReader(dp)
#      header = file.fieldnames
#      data = []

#      for row in file:
#          if row['Client'] in ("DCM222","DCD55"):
#             row["Open Authorize Quantity"] = 0
#          data.append(row)
 
# with open("dcm222.csv",'w', newline='')as dc:
#    write = csv.DictWriter(dc, fieldnames=header)
#    write.writeheader()
#    write.writerows(data)       
            

# ##UPDATE FOR SPECIFIC CODE WITH LIST DATA[]
# with open("DP_1.csv", 'r') as dp:
#      file = csv.DictReader(dp)
#      header = file.fieldnames
#      data = []

#      for row in file:
#          if row['Client'] == "DCM222":
#             row["Open Authorize Quantity"] = 0
#          data.append(row)
 
# with open("dcm222.csv",'w', newline='')as dc:
#    write = csv.DictWriter(dc, fieldnames=header)
#    write.writeheader()
#    write.writerows(data)       
            
# with open ('DP_1.csv', 'r') as dp:
#    file = csv.DictReader(dp)
#    for i in file:
#       if re.match("^WBF",i['Client']):
#          i["Open Authorize Quantity"] = 0
#          print(i)
      
#       #if i['Client'] == re.search("^WBF"):
#       #   print(i)


## WORKING
# # Open the file to read and load data into memory
# file_path =glob.glob('DP*')
# #print(file_path)


# #with open ('DP_.csv', 'r') as dp:
# with open(file_path[0], 'r') as dp:
#     file = list(csv.DictReader(dp))  # Read the CSV data into a list of dictionaries

# # Modify the rows that match the condition
# for row in file:
#     if re.match("^WBF", row['Client']):  # Check if 'Client' field starts with "WBF"
#         row["Open Authorize Quantity"] = 0  # Update the value

# # Write the updated data back to the CSV file
# with open(file_path[0], 'w', newline='') as dp:
#     # Get the fieldnames from the first row of the modified data
#     fieldnames = file[0].keys()
    
#     # Create a DictWriter and write the updated data
#     writer = csv.DictWriter(dp, fieldnames=fieldnames)
#     writer.writeheader()  # Write the header
#     writer.writerows(file)  # Write the modified rows



## WITH INPUT OUTPUT FILE NAMES
# import csv
# import re

# # Ask the user for the input and output filenames
# input_file = input("Enter the input CSV file name: ")
# output_file = input("Enter the output CSV file name: ")

# # Read the input CSV file
# with open(input_file, 'r') as dp:
#     file = list(csv.DictReader(dp))  # Read the CSV data into a list of dictionaries

# # Modify the rows that match the condition
# for row in file:
#     if re.match("^WBF", row['Client']):  # Check if 'Client' field starts with "WBF"
#         row["Open Authorize Quantity"] = 0  # Update the value

# # Write the updated data back to the output CSV file
# with open(output_file, 'w', newline='') as dp:
#     # Get the fieldnames from the first row of the modified data
#     fieldnames = file[0].keys()
    
#     # Create a DictWriter and write the updated data
#     writer = csv.DictWriter(dp, fieldnames=fieldnames)
#     writer.writeheader()  # Write the header
#     writer.writerows(file)  # Write the modified rows


                

# with open("DP_1.csv", 'r') as dp:
#    file = csv.DictReader(dp)
#    for row in file:
#     if re.match(r'^WBF',row['Client']):
#         print(row)


##Open the CSV file for reading and writing
# with open("DP_1.csv", 'r') as dp:
#     file = csv.DictReader(dp)
#     rows = []  # To store modified rows

#     # Process each row
#     for row in file:
#         if row['Client'] == "WBFT*":
#             row["Open Authorize Quantity"] = 0
#             print(row)  # Print the modified row
#         rows.append(row)  # Add the row (modified or not) to the list

# # Open the file in write mode to save the updated content
# with open("DP_1.csv", 'w', newline='') as dp:
#     fieldnames = rows[0].keys()  # Extract the header (keys)
#     writer = csv.DictWriter(dp, fieldnames=fieldnames)
#     writer.writeheader()  # Write the header
#     writer.writerows(rows)  # Write all the rows (including modified ones)

