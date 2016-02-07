#Loop Lab 3
size = int(input("What is the size of your diamond?"))
value = -2
space_value = 0
space_value_next = (size * 2) - 2
for n in range(size * 2):
    if n <= size - 1:
        for c in range((n + (n + 1)), (size * 2), 2):
            print (c, end=" ")
        for s in range(space_value):
            print (" ", end=" ")
        space_value += 2
        for x in range((size * 2 - 1), ((n + (n + 1)) - 1), -2):
            print (x, end=" ")
    else:
        value += 2
        for a in range(((size * 2) - (1 + value)), (size * 2), 2):
            print (a, end=" ")
        for p in range(space_value_next):
            print (" ", end=" ")
        space_value_next -= 2
        for b in range((size * 2 - 1), ((size * 2 - 2) - value), -2):
            print (b, end=" ")
    print ()
