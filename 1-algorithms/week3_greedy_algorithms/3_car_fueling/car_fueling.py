import random

def car_fueling(dist,miles,n,gas_stations):
  
    num_refill, curr_refill, limit = 0, 0, miles
    while limit < dist:  
        # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
          
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
            
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank 
        curr_refill += 1
        
    return num_refill

def my_car_fueling(destination, miles, gas_stations):
    position = 0
    fills = 0
    last_fill = 0
    i = 0
    if miles >= destination: return 0

    # insert start and end to the list of gas_stations
    gas_stations.append(destination)
    gas_stations.insert(0, 0)

    station_not_reached_in_a_row = 0
    while position < len(gas_stations) - 1:
        reached_furthest_gas_station = False
        while not reached_furthest_gas_station or position < len(gas_stations) - 1:
            # impossible to reach destination
            if station_not_reached_in_a_row > 1:
                return -1
            # continue if possible
            if gas_stations[i] - gas_stations[last_fill] <= miles:
                position = i
                station_not_reached_in_a_row = 0
            # can't continue, so it's necessary to fill in last gas_station
            else:
                fills += 1
                position = i - 1
                last_fill = i - 1
                i-= 1
                reached_furthest_gas_station = True
                station_not_reached_in_a_row +=1
            i += 1
        
    return fills


if __name__ == "__main__":
    # stress test
    # counter = 0
    # while True:
    #     destiny = random.randint(0, 1000)
    #     miles = random.randint(0, 1000)
    #     number_of_gas_stations = random.randint(0, 40)
    #     gas_stations = [random.randint(1, destiny + 2) for _ in range(number_of_gas_stations)]
    #     destiny += 20
    #     gas_stations.sort()
    #     res = 0
    #     res2 = 0
    #     try:
    #         res2 = car_fueling(destiny, miles, number_of_gas_stations, gas_stations)
    #         res = my_car_fueling(destiny, miles, gas_stations)
    #         assert res == res2
    #         print(f"test #{counter} passed")
    #         counter += 1
    #     except(AssertionError):
    #         print(f"test #{counter} failed")
    #         print(f"got {res} but was {res2}")
    #         print(f"data: [destination: {destiny} | miles: {miles} | gas_stations: {gas_stations} | n: {number_of_gas_stations}")
    #         break

    destiny = int(input())
    miles = int(input())
    number_of_gas_stations = int(input())
    gas_stations = input()
    gas_stations = gas_stations.split()
    gas_stations = list(map(lambda a: int(a), gas_stations))
    print(my_car_fueling(destiny, miles, gas_stations))

