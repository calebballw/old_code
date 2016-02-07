#big function
def min3(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z
print (min3(4, 7, 5))
print (min3(4, 5, 5))
print (min3(4, 4, 4))
print (min3(-2, -6, -100))
print (min3("Z", "B", "A"))
def box(y, x):
    for i in range(y):
        for n in range(x):
            print ("*", end="")
        print ()
box(7, 5)
print ()
box(3, 2)
print ()
box(3, 10)
def find(lis, key):
    n = -1
    for x in lis:
        n += 1
        if x == key:
            print ("Found", key, "at position", n)
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
find (my_list, 12)
find (my_list, 91)
find (my_list, 80)
def create_list(x):
    import random
    the_list = []
    for i in range(x):
        the_list.append(random.randrange(1, 7))
    return the_list
        
print (create_list(20))


               
def count_list(l, x):
    count = 0
    for i in l:
        if i == x:
            count += 1
    return count
coun = count_list([1,2,3,3,3,4,2,1],2)
print (coun)


def average_list(x):
    tot = 0
    for i in x:
        tot += i
    average = tot/len(x)
    return average
avg = average_list([1, 2, 3, 4])
print (avg)



y = create_list(10000)
print (count_list(y, 1))
print (count_list(y, 2))
print (count_list(y, 3))
print (count_list(y, 4))
print (count_list(y, 5))
print (count_list(y, 6))
print (average_list(y))









