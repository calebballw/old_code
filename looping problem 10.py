for n in range(9):
    for c in range(9):
        value = (c + 1) * (n + 1)
        if value < 10:
            print (" ", end="")
        print (value, end=" ")
    print ()
