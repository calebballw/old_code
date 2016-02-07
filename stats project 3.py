with open('Driving Ages/Data.txt') as f:
    my_data = f.read().splitlines()
f.close()

mn = 0
fn = 0
mh = 0
fh = 0
ml = 0
fl = 0

for x in my_data:
    if "Male" in x and "No change" in x:
        mn += 1
    elif "Female" in x and "No change" in x:
        fn += 1
    elif "Male" in x and "Higher than 16" in x:
        mh += 1
    elif "Female" in x and "Higher than 16" in x:
        fh += 1
    elif "Male" in x and "Lower than 16" in x:
        ml += 1
    elif "Female" in x and "Lower than 16" in x:
        fl += 1
print (mn)
print (fn)
print (mh)
print (fh)
print (ml)
print (fl)
print (mn + fn + mh + fh + ml + fl)
