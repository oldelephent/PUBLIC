import csv

file1 = r"1.csv" 
file2 = r"2.csv"


# with open(file1,'r')as f1, open(file2,'r')as f2:
#     read1 = tuple(csv.reader(f1))
#     read2 = tuple(csv.reader(f2))
#     for i,j in zip(read1,read2):
#         if i == j:
#             print(f"{i},{j}all good")
#         else:
#             print(f"{i},{j}not good")





####################################        color coded

# good_color = '\033[32m'  # Green
# not_good_color = '\033[31m'  # Red
# reset_color = '\033[0m'  # Reset to default color

# with open(file1, 'r') as f1, open(file2, 'r') as f2:
#     read1 = tuple(csv.reader(f1))
#     read2 = tuple(csv.reader(f2))
#     for i, j in zip(read1, read2):
#         if i == j:
#             print(f"{good_color}{i},{j} all good{reset_color}")
#         else:
#             print(f"{not_good_color}{i},{j} not good{reset_color}")
