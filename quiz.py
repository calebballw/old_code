print ("It is time for a quiz!!")
c_answers = 0

first = input("Where was Kobe born?")
if first.lower() == "italy":
    print ("Correct!")
    c_answers += 1
else:
    print ("Wrong!")

second = input("How many starwars movies are there?")
if second == "6":
    print ("Correct")
    c_answers += 1
else:
    print ("Wrong")

third = input("How many championships do the lakers have?")
if third == "16":
    print ("Correct")
    c_answers += 1
else:
    print ("Wrong")

fourth = input("How many Harry Potter books are there?")
if fourth == "7":
    print ("Correct")
    c_answers += 1
else:
    print ("Wrong")

fifth = input("How many Hobbit movies have been made?")
if fifth == "3":
    print ("Correct")
    c_answers += 1
else:
    print ("Wrong")

print ("Your are done with the quiz!!")
score = (c_answers / 5) * 100
if score > 50:
    print ("Good Job!! Your score is", score, "%")
elif score < 50:
    print ("That is just bad! Your score is", score, "%")
else:
    print ("You are right there in the middle")


 
