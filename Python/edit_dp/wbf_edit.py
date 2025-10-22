import csv
import re
import glob

## WBF DCD24 DCA74
## Client Open Authorize Quantity
##UPDATE FOR MULTIPLE CODE

finding_dp_file = glob.glob("DP*")
dp_file = ' '.join(finding_dp_file)

with open(dp_file,'r') as csvreading:
    read = csv.DictReader(csvreading)
    header = read.fieldnames

    data = []

    for i in read:
        client_row = i["Client"]

        fixed_codes  =  {"DCD24","DCA74"}
       
        if  client_row in fixed_codes or client_row.startswith("WBF")  :
            i["Open Authorize Quantity"] = 0
        data.append(i)

with open(dp_file,'w',newline='') as csvwriting:
    writing = csv.DictWriter(csvwriting,fieldnames=header)
    writing.writeheader()
    writing.writerows(data)



## ANOTHER VERSION ________________________

# finding_dp_file = glob.glob("DP*")
# dp_file = ' '.join(finding_dp_file)

# with open(dp_file, 'r') as dp:
#     file = csv.DictReader(dp)
#     header = file.fieldnames
#     data = []

#     for row in file:
#         if row['Client'].startswith("WBF") or row['Client'] in ("DCM222","DCJ35"):
#             row["Open Authorize Quantity"] = 0

#         data.append(row)

# with open(dp_file,'w',newline='')as file:
#     writer = csv.DictWriter(file,fieldnames=header)
#     writer.writeheader()
#     writer.writerows(data)







## WORKING WITH TWO CODE ______________

# with open(dp_file,'r') as csvreading:
#     read = csv.DictReader(csvreading)
#     header = read.fieldnames

#     data = []

#     for i in read:
#         if i["Client"] in ("DCD24","DCA74"):
#             i["Open Authorize Quantity"] = 0 
#         data.append(i)

# with open(dp_file,'w',newline='') as csvwriting:
#             writing = csv.DictWriter(csvwriting,fieldnames=header)
#             writing.writeheader()
#             writing.writerows(data)





