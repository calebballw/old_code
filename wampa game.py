print ("Welcome to Wampa Chase!!!")
print ("You have stolen an imperial wampa and the empire is after you.")
print ("You have to make your way across hoth 200 miles to the rebel base.")
print ("You have limited supplies.")

miles_traveled = 0
thirst = 0
wampa_tiredness = 0
empire_distance = -20
canteen_drinks = 5
done = False

while done == False:
    print ("A. Drink from your canteen.")
    print ("B. Go as fast as you can.")
    print ("C. Walk.")
    print ("D. Stop for the night.")
    print ("E. Status check.")
    print ("Q. Quit Game.")

    choice = input("What do you want to do?")
    if choice.upper() == "Q":
        done = True
        print ("Come back and play again")
    elif choice.upper() == "E":
        print ("Miles Traveled: ", miles_traveled)
        print ("Drinks in Canteen: ", canteen_drinks)
        print ("The empire is", abs(miles_traveled - empire_distance), "miles behind you.")
    elif choice.upper() == "D":
        empire_distance += 10
        if empire_distance >= miles_traveled:
            print ("You were caught and the empire is bringing you back to Darth Vader.")
            done = True
        else:
            wampa_tiredness = 0
            print ("Your wampa is happy!")
    elif choice.upper() == "B":
        miles_traveled += 15
        thirst += 2
        wampa_tiredness += 10
        empire_distance += 10
        print (miles_traveled, "miles traveled.")
    elif choice.upper() == "A":
        if canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
            print ("You are fully recharged.")
        else:
            print ("You have no more drinks in your canteen.")
    elif choice.upper() == "C":
        miles_traveled += 10
        thirst += 1
        wampa_tiredness += 5
        empire_distance += 10
        print (miles_traveled, "miles traveled.")
    else:
        print ("Invalid Choice")
    if thirst >= 4 and thirst <= 6:
        print ("You are thirsty.")
    elif thirst > 6:
        print ("You died of thirst.")
        done = True
    if wampa_tiredness >= 20 and wampa_tiredness <= 30:
        print ("Your wampa is tired.")
    elif wampa_tiredness > 30:
        print ("Your wampa died.")
        done = True
    if abs(miles_traveled - empire_distance) <= 15 and abs(miles_traveled - empire_distance) > 0:
        print ("The empire is getting close!")
    if miles_traveled >= 200:
        print ("You got to the rebel base! You win!")
        done = True
        
