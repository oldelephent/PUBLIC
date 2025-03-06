import re
import csv

file_to_read = r""
file_to_write = r""


with open(file_to_read,'r')as f1:
    file = csv.DictReader(f1)
    header = file.fieldnames
    data = []

    for row in file:
        if row['Series'] not in ["A","EQ"] or re.match("^WBF",row['Client']):
            row['Open Authorize Quantity'] = 0
        del row['Series']

        data.append(row)
            
with open (file_to_write,'w',newline='')as f2:
    write = csv.DictWriter(f2, fieldnames=header)
    write.writeheader()
    write.writerows(data)