#https://train.nzoi.org.nz/problems/800

n = int(input())

if n == 0:
    print("plausible")
    exit()
    
states = [input() for state in range(n)]
sleeping = False
exploring = False
nibbling = False
impossible = False
index = 0

if states[index] == "S":
    sleeping = True
elif states[index] == "E":
    exploring = True
elif states[index] == "N":
    nibbling = True

while index < n-1:
    index += 1
    if sleeping:
        if states[index] == "N":
            impossible = True                               
            break
        elif states[index] == "E":
            exploring, sleeping, nibbling = True, False, False
        elif states[index] == "S":
            exploring, nibbling, sleeping = False, False, True
    elif exploring:
        if states[index] == "S" or states[index] == "E":
            impossible = True
            break
        elif states[index] == "N":
            exploring, sleeping, nibbling = False, False, True
    elif nibbling:
        if states[index] == "N":
            impossible = True
            break
        elif states[index] == "E":
            exploring, sleeping, nibbling = True, False, False
        elif states[index] == "S":
            exploring, sleeping, nibbling = False, True, False

if impossible:
    print("impossible")
else:
    print("plausible")