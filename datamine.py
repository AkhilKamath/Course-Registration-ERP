import datetime, xlrd
from collections import OrderedDict
import simplejson as json
 
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('timetable.xlsx')
sh = wb.sheet_by_index(1)
 
# List to hold dictionaries
courses_list = []
 
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(3, sh.nrows):
    courses = OrderedDict()
    row_values = sh.row_values(rownum)
    courses['classcode'] = repr(row_values[0])
    courses['coursecode'] = row_values[1]
    courses['coursetitle'] = row_values[2]
    courses['creditslpu'] = row_values[3]
    courses['section'] = repr(row_values[4])
    courses['stat'] = row_values[5]
    courses['instructors'] = row_values[7]
    courses['days'] = row_values[8]
    courses['room'] = row_values[9]
    courses['compredate'] = row_values[10]
 
    courses_list.append(courses)
 
# Serialize the list of dicts to JSON
j = json.dumps(courses_list)
 
# # Write to file
# with open('data.json', 'w') as f:
#     f.write(j)

print(json.dumps(json.loads(j)[0], indent=4, sort_keys=True))