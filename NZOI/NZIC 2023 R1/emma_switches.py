#https://train.nzoi.org.nz/problems/1311

switch_no, days = map(int, input().split())
switches = [False]
switches *= switch_no
for day in range(days):
    start_switch, skip = map(int, input().split())
    start_ind = start_switch - 1
    while True:
        try:
            if switches[start_ind] == False:
                switches[start_ind] = True
                start_ind += skip
            else:
                switches[start_ind] = False
                start_ind += skip                
        except:
            break

for switch in switches:
    if switch == False:
        print("OFF")
    else:
        print("ON")
