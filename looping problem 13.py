#Looping Problem 13
for n in range(1, 18):
    value = 0
    if n <= 9:
        for x in range(9 - n):
            print (" ", end=" ")
        for c in range(1, (n + n)):
            if c <= n:
                print (c, end=" ")
            elif c > n:
                value += 1
                print ((n - value), end=" ")
    else:
        for a in range(n - 9):
            print (" ", end= " ")
        for e in range(1, (36 - (n + n))):
            if e <= (18 - n):
                print (e, end=" ")
            elif e > (18 - n):
                value += 1
                print (((18 - n) - value), end=" ")
    print ()
    
