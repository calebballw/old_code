import re
with open('Driving Ages/Data.txt') as f:
    my_data = f.read().splitlines()
f.close()
def data_count(col, row):
    p = re.compile('^\d+$')
    p1 = re.compile('^\d+.\d+$')
    count = 0
    for x in my_data:
        if col in x and ".5" not in x and row in x:
            count += 1
        elif col in x and p1.match(col) and row in x:
            count += 1
    return count

def data_count_reg(col, row):
    count = 0
    for x in my_data:
        if col in x and row in x:
            count += 1
    return count

def data(row):
    count = 0
    county = 0
    for x in my_data:
        if "Yes" in x:
            county += 1
        elif "No" in x and row in x:
            count += 1
    print (county)
    return count
print (data("No change"))
print (data("Higher than 16"))
print (data("Lower than 16"))


