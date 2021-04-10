import openpyxl, pprint

print('opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('reading rows...')
for row in range(2, sheet.max_row + 1):
    state   = sheet['B' + str(row)].value
    county  = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value

    # make sure the key for this state exists
    countyData.setdefault(state, {})
    # make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts' : 0, 'pop' : 0})

    # each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

# open a new text file and write the contents of countyData to it
print('writing results...')
resultFile = open('census2021.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('done...')