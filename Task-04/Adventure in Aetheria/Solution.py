n = int(input())
travel_times = list(map(int, input().split()))

# Find the minimum travel time to any town
min_time = min(travel_times)

# Count the number of towns with the minimum travel time
count_min_time = travel_times.count(min_time)

if count_min_time == 1:
    # If there's only one town with the minimum travel time, find its index
    town_index = travel_times.index(min_time) + 1
    print(town_index)
else:
    # If there are multiple towns with the same minimum travel time, stay in Aetheria
    print("Still Aetheria")
