import csv
from datetime import datetime, timedelta
from striprtf.striprtf import rtf_to_text
import os

employee_rtf = input("enter where rtf file will be put? ").replace("\"","")

current_date = datetime.now().strftime("%d-%m-%Y")

# Get today's date
c_date = datetime.today()

# Format the date as ddmmyyyy
formatted_date = (c_date.replace(day=1) - timedelta(days=1)).strftime("%d-%m-%Y")

salary_data = r"salary.csv"

# Read data from the salary.csv
with open(salary_data, 'r') as f1:
    reader = csv.DictReader(f1)
    
    # Iterate through each row of the CSV
    for row in reader:
        # Extract relevant data
        amount = row['Amount']
        employee_name = row['Employee_Name']
        designation = row['Designation']
        Joining_date=  row['Joining_date']

        # Create a new RTF file for each employee using their name
        employee_filename = f"{employee_rtf}/{employee_name}.rtf"
        
        with open('S.rtf','r')as rtf_content:
            # RTF content template
            data = rtf_content.read()
            
        # Write the content to the RTF file
        with open(employee_filename, 'w') as f2:
            data = data.replace('Amount', amount)
            data = data.replace('Employee_Name', employee_name)
            data = data.replace('Designation', designation) 
            data = data.replace('Date',(current_date))
            data = data.replace('Month_Year',(formatted_date))
            data = data.replace('Joining_date',Joining_date)
            
            f2.write(data)
        
        print(f"Created RTF file for {employee_name}: {employee_filename}")
