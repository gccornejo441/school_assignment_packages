from extractor import getHashTable
import datetime, ui, packages

MOVE = 'ON THE MOVE'
HUB = '@ HUB'
DELIVERD = 'DELIVERED @'

class Main:
    # CLI User option bar
    print("Welcome to the Courier Package Delivery System")
    ui.quitMsg()
    user_input = int(input("""\nFor all packet data enter enter: 1\nFor individual packet data enter: 2\nFor truck data: 3\n  """))

    if (ui.numberSwitch(user_input) >= 4):
        print("Not a valid entry.  Please enter 1, 2, or option 3.")
        exit()

    if (ui.numberSwitch(user_input) == 3):
        packages.total_recall()
        ant_input = str(input("\nType quit to terminate the program\n\nHit the enter key to continue.\n\n"))
        if(ant_input == "quit"):
            exit()

    while user_input != 'quit':

        # Var takes user time input for specified pack
        inputTime = input('Enter the time format as HH:MM:SS:\n')
        print('-' * 100)
        (hrs0, mins0, secs0) = inputTime.split(':')
        input_time = datetime.timedelta(hours=int(hrs0), minutes=int(mins0), seconds=int(secs0))

        if (user_input == 1):
            """
            Cycles through selection 1 for all packs; O(n)
            """
            try:
                for i in range(1, 41):
                    search = getHashTable().hotItem(str(i))[10]
                    hashtable = getHashTable().hotItem(str(i))[9]
                    try:
                        (hrs1, mins1, secs1) = hashtable.split(':')
                        (hrs2, mins2, secs2) = search.split(':')

                    except ValueError:
                        pass

                    deltaTime = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))

                    # Determine which packages have left the hub
                    if (deltaTime >= input_time):
                        search = HUB
                        hashtable = hashtable
                        ui.packStatus(i)
                    # Determine which packages have left but have not been delivered
                    elif (deltaTime <= input_time):
                        if (input_time < datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))):
                            search = MOVE
                            hashtable = hashtable
                            ui.packStatus(i)  

                        # If pak has been delivered then show contents.
                        else:
                            search = DELIVERD + " " + search
                            hashtable = hashtable
                            ui.packStatus(i)  
                break
            except ValueError:
                print('Not a valid entry')
                exit()
        elif (user_input == 2):
            """
            Used to cycle through selection 2 for individual packages; O(n)
            """
            try:
                i = input('Enter a valid package ID: \n')

                (hrs, mins, secs) = getHashTable().hotItem(str(i))[9].split(':')
                (hrs, mins, secs) = getHashTable().hotItem(str(i))[10].split(':')

                deltaTime = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                # Loops through packages and dictates which packets are left and need to be delivered
                if (deltaTime >= input_time):
                    search = HUB
                    hashtable = getHashTable().hotItem(str(i))[9]
                    ui.packStatus(i)
                elif (deltaTime <= input_time):
                    if (input_time < deltaTime):
                        search = MOVE
                        hashtable = getHashTable().hotItem(str(i))[9]
                        ui.packStatus(i)
                    else:
                        search = DELIVERD + search
                        hashtable = getHashTable().hotItem(str(i))[9]
                        ui.packStatus(i)

            except ValueError:
                print('Not a valid entry.')
                exit()
        else:
            print('Not a valid entry.')
            exit()

