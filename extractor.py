import csv
from dataStrut import DataStrut
import lib


with open('sheets/packets_data.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')

    table = DataStrut()  # Create an instance of HashTable class
    
    def insert(key, item):
        key_value = [key, item]
        table.bucket_list(key).append(key_value)
        return True

    truckOne = []  # packets list assigned to truck 1
    truckTwo = []  # packets list assigned to truck 2
    truckThree = []  # packets list assigned to truck 3

    # Insert values from csv file into key/value pairs of the hash table -> O(n)
    for row in read_csv:
        id = row[0]
        street = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        notes = row[7]
        start = ''
        location = ''
        status = '@ HUB'
        value = [
            id,
            location,
            street,
            city,
            state,
            zip,
            delivery,
            size,
            notes,
            start,
            status
            ]

        # following are filters to assign packets to truck
        # the packets are assigned to truck manually based on similarity (patterns) or packet's feathers

        # Insert value into the hash table
        lib.filter(
            truckOne,
            truckTwo,
            truckThree, 
            value
        )
        insert(id, value)

    ## retrives packs at O(1)
    def getHashTable():
        return table

    # Get packets list assigned to truck 1  :> O(1)
    def getTruckList():
        return truckOne


    # Get packets list assigned to truck 2  :> O(1)
    def assignPacks():
        return truckTwo


    # Get packets list assigned to truck 3  :> O(1)
    def getPacks():
        return truckThree

