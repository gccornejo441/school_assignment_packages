import distances
import extractor
import schema

# ================================================= first truck ======================================================

# set delivery start time to packets of truck 1   :> O(n)
for index, value in enumerate(extractor.getTruckList()):
    extractor.getTruckList()[index][9] = ['8:00:00'][0]
    schema.kellie.append(extractor.getTruckList()[index])

# Compare first truck addresses to full address list :> O(n^2)
for index, outer in enumerate(schema.kellie):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            schema.kellieDist.append(outer[0])
            schema.kellie[index][1] = inner[0]

# Call greedy  algorithm to sort packages for first truck
distances.find_fastest_route(schema.kellie, 1, 0)
total_distance_tr1 = 0

# Calculate :> O(n)
# 1.Total distance of the First truck
# 2.distance of each packages
for index in range(len(distances.getFirstIndexList(1))):
    try:
        total_distance_tr1 = distances.getDistance(int(distances.getFirstIndexList(1)[index]),
                                                    int(distances.getFirstIndexList(1)[index + 1]),
                                                    total_distance_tr1)

        deliver_package = distances.get_time(
            distances.getCurrent(int(distances.getFirstIndexList(1)[index]),
                                           int(distances.getFirstIndexList(1)[index + 1])),
            ['8:00:00'])
        distances.getFirstIndexList(0)[index][10] = (str(deliver_package))
        extractor.getHashTable().update(int(distances.getFirstIndexList(0)[index][0]), schema.kellie)
    except IndexError:
        pass

# ================================================= Second truck ======================================================

# set delivery start time to packets of truck 1   :> O(n)
for index, value in enumerate(extractor.assignPacks()):
    extractor.assignPacks()[index][9] = ['9:10:00'][0]
    schema.wilson.append(extractor.assignPacks()[index])

# Compare Second truck addresses to full address list :> O(n^2)
for index, outer in enumerate(schema.wilson):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            schema.wilsonDist.append(outer[0])
            schema.wilson[index][1] = inner[0]

# Call greedy  algorithm to sort packages for Second truck
distances.find_fastest_route(schema.wilson, 2, 0)
total_distance_tr2 = 0

# Calculate :> O(n)
# 1.Total distance of the Second truck
# 2.distance of each package
for index in range(len(distances.getSecIndexList(1))):
    try:
        total_distance_tr2 = distances.getDistance(int(distances.getSecIndexList(1)[index]),
                                                    int(distances.getSecIndexList(1)[index + 1]),
                                                    total_distance_tr2)

        deliver_package = distances.get_time(
            distances.getCurrent(int(distances.getSecIndexList(1)[index]),
                                           int(distances.getSecIndexList(1)[
                                                   index + 1])), ['9:10:00'])
        distances.getSecIndexList(0)[index][10] = (str(deliver_package))
        extractor.getHashTable().update(int(distances.getSecIndexList(0)[index][0]), schema.wilson)
    except IndexError:
        pass

# ================================================= Third truck ======================================================

# set delivery start time to packets of truck 3   :> O(n)
for index, value in enumerate(extractor.getPacks()):
    extractor.getPacks()[index][9] = ['11:00:00'][0]
    schema.subyam.append(extractor.getPacks()[index])

# Compare Third truck addresses to full address list :> O(n^2
for index, outer in enumerate(schema.subyam):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            schema.subyamDist.append(outer[0])
            schema.subyam[index][1] = inner[0]

# Call greedy  algorithm to sort packages for Third truck
distances.find_fastest_route(schema.subyam, 3, 0)
total_distance_tr3 = 0

# Calculate :> O(n)
# 1.Total distance of the Third truck
# 2.distance of each package
for index in range(len(distances.getThirdIndexList(1))):
    try:
        total_distance_tr3 = distances.getDistance(int(distances.getThirdIndexList(1)[index]),
                                                    int(distances.getThirdIndexList(1)[index + 1]),
                                                    total_distance_tr3)

        deliver_package = distances.get_time(
            distances.getCurrent(int(distances.getThirdIndexList(1)[index]),
                                           int(distances.getThirdIndexList(1)[index + 1])),
            ['11:00:00'])
        distances.getThirdIndexList(0)[index][10] = (str(deliver_package))
        extractor.getHashTable().update(int(distances.getThirdIndexList(0)[index][0]), schema.subyam)
    except IndexError:
        pass


# Get the total distance of all 40 packages :> O(1)
def total_distance_all_tr():
    return total_distance_tr1 + total_distance_tr2 + total_distance_tr3

truckOne = total_distance_tr1
truckTwo = total_distance_tr2
truckThree = total_distance_tr3
def total_recall():
    print("Truck 1: Total distance: %s" %(round(truckOne, 1)))
    print("Truck 2: Total distance: %s" %(round(truckTwo, 1)))
    print("Truck 3: Total distance: %s" %(round(truckThree, 1)))
    print("Total distance by all trucks: %s" %(round(total_distance_all_tr(), 1)))