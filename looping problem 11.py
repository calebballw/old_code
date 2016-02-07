#Looping Problem 11
for n in range(1, 10):
    value = 0
    for x in range(9 - n):
        print (" ", end=" ")
    for c in range(1, (n + n)):
        if c <= n:
            print (c, end=" ")
        else:
            value += 1
            print ((n - value), end=" ")
    print ()
