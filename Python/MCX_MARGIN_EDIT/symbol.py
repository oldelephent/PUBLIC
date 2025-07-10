import os
from datetime import datetime
import xlrd
from xlutils.copy import copy

os.remove(r"\SymbolMargin.xls")
os.rename(r"\REPORTS.xls",r"\SymbolMargin.xls")

edit_file = "SymbolMargin.xls"

# Get current date formatted as DD-MM-YYYY
today = datetime.now()
formatted_date = today.strftime('%d-%m-%Y')

# Open the original .xls file with formatting_info=True to preserve formatting
rb = xlrd.open_workbook(edit_file, formatting_info=True)

# Access the first sheet by index
sheet = rb.sheet_by_index(0)

# Copy workbook for writing
wb = copy(rb)
w_sheet = wb.get_sheet(0)  # Get writable sheet

# Write into the top-left cell of the merged cell (e.g., B1 = row 0, col 1)
w_sheet.write(0, 1, f'Symbol wise Margin % - MCX {formatted_date}')

# Save the modified workbook to a new file
wb.save(edit_file)

print(f"Updated file saved as {edit_file}")

