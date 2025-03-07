import csv
import re
import glob

file_path =glob.glob('SERIES*')[0]
dp_file_name = (file_path).replace("SERIES_",'')

with open(file_path,'r')as f1:
    file = csv.DictReader(f1)
    header = file.fieldnames
    data = []

    for row in file:
        if row['Series'] not in ["A","EQ"] or re.match("^WBF",row['Client']):
            row['Open Authorize Quantity'] = 0
        del row['Series']
        data.append(row)
                
with open (dp_file_name,'w',newline='')as f2:
    write = csv.DictWriter(f2, fieldnames=header)
    write.writeheader()
    write.writerows(data)

