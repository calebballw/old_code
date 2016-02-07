def adventure():
    room_list = []
    room = ["You are in your cell. There is a passage to the north, south, east, west.", 3, 2, 4, 1]
    room_list.append(room)

    room = ["You are in the second jail cell. There is a passage to the north and east.", 6, 0, None, None]
    room_list.append(room)

    room = ["You are in the room of guards. There is a passage to the south and west.", None, None, 9, 0]
    room_list.append(room)

    room = ["You are in the exit hallway. There is a passage to the north, south, east, west.", 13, 5, 0, 6]
    room_list.append(room)

    room = ["You are in the Dragon's Cave. The Dragon is dead. There is a passage to the north and south.", 0, None, 8, None]
    room_list.append(room)

    room = ["You are in the Great Room. There is a passage to the west.", None, None, None, 3]
    room_list.append(room)

    room = ["You are in the cafeteria. There is a passage to the south and east.", None, 3, 1, None]
    room_list.append(room)

    room = ["You are in the Training Room. There is a passage to the east and south.", None, 8, 12, None]
    room_list.append(room)

    room = ["You are in the Torture Chamber. There is a passage to the north, south, east, and west.", 4, 9, 11, 7]
    room_list.append(room)

    room = ["You are in the back hallway. There is a passage to the north, south, and west.", 2, None, 10, 8]
    room_list.append(room)

    room = ["You entered the Lava Pit, you burned alive."]
    room_list.append(room)

    room = ["You are in the execution room. There is a passage to the north.", 8, None, None, None]
    room_list.append(room)

    room = ["You are in the weapon's room. There is a passage to the north.", 7, None, None, None]
    room_list.append(room)
    current_room = 0
    dragon = "Death"

    print ("Welcome to the Dungeon Adventure Game!")
    print ("You are trapped in a horrific dungeon and you are trying to escape!")
    print ("Get out of the building without dying and you win!")
    done = False
    while done == False:
        print ()
        print (room_list[current_room][0])
        decision = input("Where do you want to go? Press q if you want to quit.")
        if decision == "north":
            next_room = room_list[current_room][1]
            if next_room == None:
                print ("You cannot go that way.")
            elif next_room == 4:
                print ("The dragon's cave is locked.")
                passcode_d = input("What is the passcode? Type back to go back.")
                if passcode_d == "fvbg":
                    if dragon == "Life":
                        print ("You defeated the dragon and have the exit codes!")
                        print ("Password: jfkdhg")
                        current_room = next_room
                    else:
                        print ("The dragon burned you alive!")
                        done = True
                elif passcode_d == "back":
                    print ("Wimp")
                else:
                    print ("Wrong! You were executed!")
                    done = True
            elif next_room == 3:
                print ("You have found the passcode to the weapons room.")
                print ("Password: cOpEnHaGeN")
                current_room = next_room
            elif next_room == 13:
                print ("The exit door is locked.")
                passcode = input("What is the passcode? Type back to go back.")
                if passcode == "jfkdhg":
                    print ("You escaped the prison!!!")
                    done = True
                elif passcode == "back":
                    print ("wimp")
                else:
                    print ("Wrong!! The alarms sounded and you were executed!")
                    done = True
            else:
                current_room = next_room
        elif decision == "east":
            next_room = room_list[current_room][2]
            if next_room == None:
                print ("You cannot go that way.")
            else:
                current_room = next_room
        elif decision == "west":
            next_room = room_list[current_room][4]
            if next_room == None:
                print ("You cannot go that way.")
            else:
                current_room = next_room
        elif decision == "south":
            next_room = room_list[current_room][3]
            if next_room == None:
                print ("You cannot go that way.")
            elif next_room == 12:
                print ("The weapon's room is locked.")
                passcode_w = input("What is the passcode? Type back to go back.")
                if passcode_w == "cOpEnHaGeN":
                    print ("Congratulations! You have weapons to beat the dragon.")
                    dragon = "Life"
                    current_room = next_room
                elif passcode_w == "back":
                    print ("wimp")
                else:
                    print ("Wrong! The alarms sounded and the guards found you and executed you.")
                    done = True
            elif next_room == 4:
                print ("The dragon's cave is locked.")
                passcode_d = input("What is the passcode? Type back to go back.")
                if passcode_d == "fvbg":
                    if dragon == "Life":
                        print ("You defeated the dragon and have the exit codes!")
                        print ("Password: jfkdhg")
                        current_room = next_room
                    else:
                        print ("The dragon burned you alive!")
                        done = True
                elif passcode_d == "back":
                    print ("wimp")
                else:
                    print ("Wrong! The alarms sounded and the guards found you and threw you in the lava pit.")
                    done = True
            elif next_room == 10:
                print ("You were burned alive in the lava pit!")
                done = True
            elif next_room == 11:
                print ("You have found the password to the dragon's cave.")
                print ("Password: fvbg")
            else:
                current_room = next_room
        elif decision == "q":
            done = True
        else:
            print ("That is not an option!")

adventure()

d_for_good = False
while d_for_good == False:
    a = input("Do you want to play again?")
    if a == "yes":
        adventure()
    if a == "no":
        d_for_good = True
            
            
