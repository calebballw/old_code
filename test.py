with open('Driving Ages/Data.txt') as f:
    my_data = f.read().splitlines()
f.close()
s = "hi i am caleb"
for x in s:
    if x == "hi":
        print (x, end="")
