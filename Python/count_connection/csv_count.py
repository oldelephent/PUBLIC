import os
import csv

read_one = r"codes.txt"
# xls_files = r""
# xl_files = os.listdir(xls_files)

xl_files = os.listdir(os.getcwd())

with open(read_one, 'r') as f1:
    blank_list = []
    for line in f1:
        blank_list.append(line.strip())

for read_one in blank_list:
    count = 0

    for i in xl_files:
        if i.endswith('.csv'):

            with open(i, 'r') as f2:
                reader = csv.DictReader(f2)
                for row in reader:
                    if read_one == row['UserID']:
                        count += 1

    with open('output.csv', 'a', newline='') as output_file:                                
                            writer = csv.writer(output_file)
                            writer.writerow([read_one, count])  
                            print(f"Processed {read_one}: {count} occurrences found.")
                            
