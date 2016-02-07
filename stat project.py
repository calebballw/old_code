with open('class_input.txt') as f:
    my_data = f.read().splitlines()
f.close

count_nc = 0
h = 0
l = 0
for x in my_data:
    if x == "No change":
        count_nc += 1
    elif x == "Higher than 16":
        h += 1
    else:
        l += 1
print ("No change is ", count_nc)
print ("Higher is ", h)
print ("Lower is ", l)
