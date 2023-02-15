import openpyxl

excel_file = ['Utilizatori/ANDREI/Descarcari/Excelfile1.xlsx']

values = []

for file in excel_file:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook('N')