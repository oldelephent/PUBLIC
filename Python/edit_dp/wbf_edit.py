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

## WORKING WITH TWO CODE

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





