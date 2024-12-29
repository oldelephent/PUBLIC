
file_path = input("enter path:  ").strip('\"')

with open (file_path, 'r') as file:
    file_data = file.read().upper()
    
with open (file_path,'w') as new_file:
    new_file.write(file_data)
    


