from extractor import getHashTable

# Works in O(1) to display pack information.
def packStatus(count):
    PACK = getHashTable().hotItem(str(count))[0]
    LOAD = getHashTable().hotItem(str(count))[9]
    DELIVER = getHashTable().hotItem(str(count))[10]
    print(
        '-' * 80,
         "\nPack id number: %s"
          "\nLoad time: %s\n"
          u"\u001b[31mStatus: %s\n"
           u"\u001b[0m"
        %(PACK, LOAD, DELIVER)
        )

def quitMsg():
    return print("\nEnter 'quit' at anytime to quit session.\n")

def numbers_to_strings(user_input):
        switcher = {
            1: 1,
            2: 2,
            3: 3,
        }
        return switcher.get(user_input, 4)

# Delivery Status
HUBSTATUS = '@ HUB'
