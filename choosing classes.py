import sys
classes = ['Math', 'English', 'AP']
print ("Choose a class")
def choices():
    while 1 == 1:
        print (classes)
        choice = input("Choose class 1: ")
        if choice == 'Math' or choice == 'English':
            print ('Good 1st Choice')
            break
        elif choice == 'AP':
            while 4 == 4:
                choice3 = input("That is a really hard class. Are you sure you want to take it? Yes/No ")
                if choice3 == 'Yes':
                    print ('Wow you must be smart.')
                    break
                elif choice3 == 'No':
                    print ('I knew you could not take hard classes')
                    choices()
                else:
                    print ('invalid choice')
                    continue
        else:
            print ('invalid choice')
            continue
choices()
        
def choices2(choice):
    while 2 == 2:
        print (classes)
        choice2 = input("Choose class 2: ")
        if choice2 == choice:
            print ('You already chose that one')
            continue
        elif choice2 == 'Math' or choice2 == 'English':
            print ("Good Choice")
            break
        elif choice2 == 'AP':
            while 3 == 3:
                choice4 = input("That is a really hard class. Are you sure you want to take it? Yes/No ")
                if choice4 == 'Yes':
                    print ('Wow you must be smart')
                    sys.exit()
                elif choice4 == 'No':
                    print ('I knew you could not take it')
                    choices2()
                else:
                    print ('Invalid Choice')
                    continue
    else:
        print ('Invalid Choice')
choices2()
print ("Congratulations. You just completed you course registration. If you want to redo your course registration, that stinks for you because there are no redos!!!!")
            
