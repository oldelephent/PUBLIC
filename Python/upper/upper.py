
file_path = input("enter path:  ").strip('\"')

with open (file_path, 'r') as file:
    read = file.read()
    upper_file = read.upper()

with open (file_path,'w') as new_file:
    new_file.write(upper_file)
    



