import csv
import datetime

with open('sheets/distance_data.csv') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))

with open('sheets/address_data.csv') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))


    ## Get package address data -> O(n)
    def get_address():
        return distance_name_csv

    def getDistance(row, col, total):  ## gets the total distance from given row/column value:> O(1)
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]
        return total + float(distance)

    def getCurrent(row, col):  ## gets the current distance of given truck:>  O(1)
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]
        return float(distance)
    
    def get_time(distance, truck_list):  ## Calculate total distance for a given truck -> O(n)
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total

    ## packets and index lists will be filled
    TRUCK1LIST, TRUCK2LIST, TRUCK3LIST = ([] for i in range(3))
    TRUCK1SORT, TRUCK2SORT, TRUCK3SORT = ([] for i in range(3))


    ## Problem solving heuristic algorithm running at O(n^2)
    def find_fastest_route(_list, num, curr_location):
        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0
        ## loops through input list O(n)
        for i in _list:
            value = int(i[1])
            if getCurrent(curr_location, value) <= lowest_value:
                lowest_value = getCurrent(
                    curr_location, value)
                location = value
        ## loops through input list O(n)
        for i in _list:
            if getCurrent(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    TRUCK1LIST.append(i)
                    TRUCK1SORT.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    find_fastest_route(_list, 1, curr_location)
                elif num == 2:
                    TRUCK2LIST.append(i)
                    TRUCK2SORT.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    find_fastest_route(_list, 2, curr_location)
                elif num == 3:
                    TRUCK3LIST.append(i)
                    TRUCK3SORT.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    find_fastest_route(_list, 3, curr_location)

    ## Insert 0 for the first index of each index list
    TRUCK1SORT.insert(0, '0')
    TRUCK2SORT.insert(0, '0')
    TRUCK3SORT.insert(0, '0')

    ## O(1) sorts and list 
    def getFirstIndexList(num):
        if (num == 1):
            return TRUCK1SORT
        else:
            return TRUCK1LIST
    
    def getSecIndexList(num):
        if (num == 1):
            return TRUCK2SORT
        else:
            return TRUCK2LIST

    def getThirdIndexList(num):
        if (num == 1):
            return TRUCK3SORT
        else:
            return TRUCK3LIST

