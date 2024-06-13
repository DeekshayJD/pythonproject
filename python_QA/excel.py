from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Create a new sheet
ws = wb.create_sheet(title="NewSheet")

# Save the workbook
wb.save("example.xlsx")
