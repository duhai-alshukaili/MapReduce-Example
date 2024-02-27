import sys

employee = {}

for line  in sys.stdin:
    line = line.strip()
    empname, dept = line.split("\t")
    try:
        employee[dept] = employee[dept] + 1
    except:
        employee[dept] = 1

for x in employee.keys():
    print("{0}\t{1}".format(x, employee[x]))
