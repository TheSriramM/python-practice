#https://train.nzoi.org.nz/problems/1133

""""""

r_types, player_no, tiles = map(int, input().split())
start_pos = []
rocket_types = {}
#append the rocket types to a dictionary
for i in range(r_types):
    cost, fuel = map(int, input().split())
    rocket_types[cost] = fuel
#find the starting position of each player
for i in range(player_no):
    start_pos.append(int(input()))
print(start_pos)