#! python3
# readCensueExcel.py - tabulates population and number of census tracts for each county

import openpyxl
import pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

for i in range(2, sheet.max_row + 1):
    state = sheet['B' + str(i)].value
    county = sheet['C' + str(i)].value
    pop = sheet['D' + str(i)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)
    #理解：当key（state、county）相同时，仍保留当前变量值（state、county），然后顺序执行脚本，tracts会加1，pop会加上新生成的pop的值；当key（state、county）不同，即不同的周或县时，会生成新的字典，再循环

# print(pprint.pformat(countyData))

file = open('census2010.py', 'w')
file.write(pprint.pformat(countyData))
file.close()

wb.remove()
wb.remove_sheet