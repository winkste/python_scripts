import openpyxl

wb = openpyxl.load_workbook('../empty_book1.xlsx')

sheets = wb.get_sheet_names()

print(sheets)

sheet = wb.get_sheet_by_name('Projects')

print(sheet['B4'].value)

for rowOfCellObjects in sheet['B3':'E5']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('---END OF ROW ---')



