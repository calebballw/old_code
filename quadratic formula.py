# Quadratic Solver

import math

while 1 == 1:
    

    a = int(input("Type value of a: "))
    b = int(input("Type value of b: "))
    c = int(input("Type value of c: "))

    d = b**2 -4*a*c

    if d < 0:
        print ("No Real Solution")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        print ("One solution:"), x
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        print ("This equation has two solutions")
        print (x1)
        print (x2)
