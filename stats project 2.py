with open('Driving Ages/Data.txt') as f:
    my_data = f.read().splitlines()
f.close()
j = 0
S = 0
s = 0
f = 0
t = 0
g = 0
c = 0
v = 0
b = 0
gh = 0
fg = 0
ff = 0
dd = 0
for x in my_data:
    if "Junior" in x and "No change" in x:
        j += 1
    elif "Senior" in x and "No change" in x:
        S += 1
    elif "Sophomore" in x and "No change" in x:
        s += 1
    elif "Freshman" in x and "No change" in x:
        f += 1
    elif "Junior" in x and "Higher than 16" in x:
        g += 1
    elif "Senior" in x and "Higher than 16" in x:
        c += 1
    elif "Sophomore" in x and "Higher than 16" in x:
        v += 1
    elif "Freshman" in x and "Higher than 16" in x:
        b += 1
    elif "Junior" in x and "Lower than 16" in x:
        gh += 1
    elif "Senior" in x and "Lower than 16" in x:
        fg += 1
    elif "Sophomore" in x and "Lower than 16" in x:
        ff += 1
    elif "Freshman" in x and "Lower than 16" in x:
        dd += 1
    
print ("The amount of juniors who said no change is ", j)
print ("No change Seniors = ", S)
print ("No change Sophomores = ", s)
print ("No change Freshman = ", f)
print (g)
print (c)
print (v)
print (b)
print (gh)
print (fg)
print (ff)
print (dd)
print (j + S + s + f + g + c + v + b + gh + fg + ff + dd)


