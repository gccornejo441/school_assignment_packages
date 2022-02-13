def filter(truck, truck2, truck3, val):
    if ("EOD" not in val[6]):
        if ('Delayed on flight---will not arrive to depot until 9:05 am' in val[8] or '3365 S 900 W' in val[2]):
            truck.append(val)
        elif ('3365 S 900 W' in val[2]):
            truck.append(val)
        else:
            truck2.append(val)
    
    if ('EOD' in val[6]) and ('none' not in val[8]):
            if ('Wrong address listed' in val[8]):
                truck3.append(val)
            elif ('84103' in val[5]):
                truck3.append(val)
            else:
                truck2.append(val)

    if ('EOD' in val[6]) and ('none' in val[8]):
            if '177 W Price Ave' in val[2] or '2010 W 500 S' in val[2] or '1330 2100 S' in val[2] or \
                    ('3575 W Valley Central Station bus Loop' in val[2]) or ('3148 S 1100 W' in val[2]):
                truck.append(val)

            else:
                if ('84103' in val[5]) or ('84111' in val[5]) or ('84117' in val[5]) or ('84119' in val[5]):
                    if ('300 State St' in val[2]):
                        truck3.append(val)
                    else:
                        truck2.append(val)
                else:
                    truck3.append(val)
