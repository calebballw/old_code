#Loop Lab 2
size = int(input("What is the size of the box?"))
for n in range(size):
    if n == 0 or n == size - 1:
        for c in range(size * 2):
            print ("o", end="")
    else:
        print ("o", end="")
        for x in range((size * 2) - 2):
            print (" ", end="")
        print ("o", end="")
    print ()
