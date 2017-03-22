#! python3
# updateProduce.py - corrects costs in produce sales spreadsheet

import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}     #活用字典，减少if判断，且便于后期修改，见书P231

for i in range(2, sheet.max_row+1):
    if sheet['A' + str(i)].value in PRICE_UPDATES:
        sheet['B' + str(i)].value = PRICE_UPDATES[sheet['A' + str(i)].value]

wb.save('updateProduceSale.xlsx')