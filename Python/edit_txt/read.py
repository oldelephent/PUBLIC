import time

first_file = r"E:\ABHISHEK\WORKING\python\VISHWAS\txt\Fin_Exp14012025.txt"
second_file = r"E:\ABHISHEK\WORKING\python\VISHWAS\txt\T3 DEP20250114.txt"
final_file = r"E:\ABHISHEK\WORKING\python\VISHWAS\txt\test.txt"


# #reading writing first file
# with open(first_file,'r',encoding='UTF-16')as f1:
#     a = f1.read()

#     with open(final_file,'w')as f3:
#         f3.write(a)

# #reading writing first file
# with open(second_file,'r',encoding='UTF-16')as f1:
#     a = f1.read()

#     with open(final_file,'w')as f3:
#         f3.write(a)

# ##reading writing second file
# with open(second_file,'r')as f2:
#     #a = f2.read().replace('|',',')
#     #a = f2.read()[14:]
#     a = f2.read()[14:].replace('|',',')
#     #print(a)

#     with open('2nd.txt','w')as f3:
#         f3.write(a)


## fully wokring with both file reading and writing replacing | to , and removing two code
with open(first_file, 'r',encoding='UTF-16')as f1, open(second_file,'r')as f2: #reading both line seprate
    with open(final_file,'w',newline='\n')as f3:                               #opening for writing
        f3.write(f1.read())                                                    #writing first file
        f3.write(f2.read()[14:].replace('|',','))                              #wirting second file replacing | with, remove begening 2 code



## wokring with both file reading and writing
# with open(first_file, 'r',encoding='UTF-16')as f1, open(second_file,'r')as f2:
#     with open(final_file,'w',newline='\n')as f3:
#         f3.write(f1.read())
#         f3.write(f2.read())


# import chardet

# with open(first_file, 'rb') as f:
#     raw_data = f.read()
#     result = chardet.detect(raw_data)
#     print(result)

# # wokring with both file reading and writing
# with open(first_file, 'r',encoding='UTF-16')as f1, open(second_file,'r')as f2:
#     with open(final_file,'w',newline='\n')as f3:
#         f3.write(f1.read())
#         f3.write(f2.read().replace('|',','))


# with open(second_file,'r')as f1:
#     a = f1.read().replace('|',',')
#     print(a)












# with open(first_file,'r') as f1, open(second_file,'r')as f2:
#     a = f1.read()
#     b = f2.read()

#     with open("test.txt",'w',newline='\n')as f3:
#         f3.write(a)
#         f3.write(b)


# with open(first_file, 'r',encoding='UTF-16')as f1, open(second_file,'r',encoding='UTF-16-LE')as f2:
#     # for i in f2:
#     #     print(i)
#     #with open(final_file,'w',newline='\n',encoding='utf-8')as f3:
#     with open(final_file,'w',encoding='UTF-16-LE')as f3:
#         #f3.write(f1.read())
#         f3.write("\n")
#         f3.write(f2.read())

