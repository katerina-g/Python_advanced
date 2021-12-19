def flights(*args):
    flight_dict = {}
    for i in range(0, len(args), 2):
        if args[i] == "Finish":
            break
        key = args[i]
        value = int(args[i + 1])
        if key in flight_dict:
            flight_dict[key] += value
        else:
            flight_dict[key] = value

    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))