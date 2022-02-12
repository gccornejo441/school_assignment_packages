import csv
from dataStrut import DataStrut
import lib

table = DataStrut()  # Create an instance of HashTable class
    
def insert(key, item):
    key_value = [key, item]
    table.numList(key).append(key_value)
    return True

with open('sheets/packets_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    truckOne = []  # packets list assigned to truck 1
    truckTwo = []  # packets list assigned to truck 2
    truckThree = []  # packets list assigned to truck 3

    # Reads from CSV at Big O(n)
    for row in reader:
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
    def getTruckList():
        return truckOne
    def assignPacks():
        return truckTwo
    def getPacks():
        return truckThree

