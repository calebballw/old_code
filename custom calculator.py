while 1 == 1:
    
    print ("a. Temperature")
    print ("b. Trapezoid")
    print ("c. Gravity")

    initial_question = input("Which calculator do you want?")

    if initial_question == "a":
        f = input("Put in temperature in Farenheit:")
        f = float(f)
        c = (f - 32) * (5 / 9)
        print (c, "degrees celcius")
    elif initial_question == "b":
        h = float(input("Enter height in inches of Trapezoid:"))
        length_bottom = float(input("Enter length in inches of bottom base:"))
        length_top = float(input("Enter length in inches of top base:"))
        area = (1 / 2) * (length_bottom + length_top) * h
        print (area, "inches")
    elif initial_question == "c":
        mass = float(input("Enter the mass of your object:"))
        fg = mass * 9.8
        print ("Your weight force is", fg, "newtons.")

    
