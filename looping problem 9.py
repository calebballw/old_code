#Looping Problem 9
for n in range(11):
    for c in range(n):
        print (" ", end=" ")
    for c in range(10 - n):
        print (c, end=" ")
    print ()
