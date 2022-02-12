import distances
import extractor
import schema

totalDistance = [0, 0, 0]
truckIdx = [0, 0, 0, 0, 0, 0]

# Loops through an enumerated trucklist O(n) 
for index, value in enumerate(extractor.getTruckList()):
    extractor.getTruckList()[index][9] = ['8:00:00'][0]
    schema.kellie.append(extractor.getTruckList()[index])

# Loops through twice at O(n^2) for set truck delivery
for index, outer in enumerate(schema.kellie):
    for inner in distances.get_address():
        if (outer[2] == inner[2]):
            schema.kellieDist.append(outer[0])
            schema.kellie[index][1] = inner[0]

# Call greedy  algorithm to sort packages for first truck O(n^2)
distances.find_fastest_route(schema.kellie, 1, 0)

truckIdx[0] = distances.getFirstIndexList(1)
truckIdx[1] = distances.getFirstIndexList(0)
# Big O(n) for loop through truck load [array]

for index in range(len(truckIdx[0])):
    try:
        totalDistance[0] = distances.getDistance(int(truckIdx[0][index]), int(truckIdx[0][index + 1]), totalDistance[0])

        deliver_package = distances.get_time(distances.getCurrent(int(truckIdx[0][index]), int(truckIdx[0][index + 1])), ['8:00:00'])
        truckIdx[1][index][10] = (str(deliver_package))
        extractor.getHashTable().adjuster(int(truckIdx[1][index][0]), schema.kellie)
    except IndexError:
        pass

# Second truck 

# Loops through an enumerated trucklist O(n) 
for index, value in enumerate(extractor.assignPacks()):
    extractor.assignPacks()[index][9] = ['9:10:00'][0]
    schema.wilson.append(extractor.assignPacks()[index])

# Loops through twice at O(n^2) for set truck delivery
for index, outer in enumerate(schema.wilson):
    for inner in distances.get_address():
        if (outer[2] == inner[2]):
            schema.wilsonDist.append(outer[0])
            schema.wilson[index][1] = inner[0]

# Call greedy  algorithm to sort packages for Second truck
distances.find_fastest_route(schema.wilson, 2, 0)

# Big O(n) for loop through truck load [array]
truckIdx[2] = distances.getSecIndexList(1)
truckIdx[3] = distances.getSecIndexList(0)

for index in range(len(truckIdx[2])):
    try:
        totalDistance[1] = distances.getDistance( int(truckIdx[2][index]), int(truckIdx[2][index + 1]), totalDistance[1])

        deliver_package = distances.get_time(
            distances.getCurrent(int(truckIdx[2][index]), int(truckIdx[2][index + 1])), ['9:10:00'])
        truckIdx[3][index][10] = (str(deliver_package))
        extractor.getHashTable().adjuster(int(truckIdx[3][index][0]), schema.wilson)
    except IndexError:
        pass


# Loops through an enumerated trucklist O(n) 
for index, value in enumerate(extractor.getPacks()):
    extractor.getPacks()[index][9] = ['11:00:00'][0]
    schema.subyam.append(extractor.getPacks()[index])

# Will run through enumerated list @ O(n^2) to compare delivery address to address list
for index, outer in enumerate(schema.subyam):
    for inner in distances.get_address():
        if (outer[2] == inner[2]):
            schema.subyamDist.append(outer[0])
            schema.subyam[index][1] = inner[0]

# Call greedy  algorithm to sort packages for Third truck
distances.find_fastest_route(schema.subyam, 3, 0)
total_distance_tr3 = 0

# Big O(n) for loop through truck load [array]
truckIdx[4] = distances.getThirdIndexList(1)
truckIdx[5] = distances.getThirdIndexList(0)
for index in range(len(truckIdx[4])):
    try:
        totalDistance[2] = distances.getDistance(int(truckIdx[4][index]), int(truckIdx[4][index + 1]), totalDistance[2])

        deliver_package = distances.get_time(distances.getCurrent(int(truckIdx[4][index]),int(truckIdx[4][index + 1])), ['11:00:00'])
        truckIdx[5][index][10] = (str(deliver_package))
        extractor.getHashTable().adjuster(int(truckIdx[5][index][0]), schema.subyam)
    except IndexError:
        pass

## ----------------------------------Displays Package Data------------------------------------ ##

def total_distance_all_tr():
    return totalDistance[0] + totalDistance[1] + totalDistance[2]

def total_recall():
    print("Truck 1: Total distance: %s" %(round(totalDistance[0], 1)))
    print("Truck 2: Total distance: %s" %(round(totalDistance[1], 1)))
    print("Truck 3: Total distance: %s" %(round(totalDistance[2], 1)))
    print("Total distance by all trucks: %s" %(round(total_distance_all_tr(), 1)))

## ------------------------------------------------------------------------------------------- ##