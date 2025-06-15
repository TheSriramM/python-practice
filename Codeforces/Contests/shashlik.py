n = int(input())
output = []
for _ in range(n):
    temp, req1, req2, dec1, dec2 = map(int, input().split())
    tot = 0
    if dec1 < dec2:
        # while temp >= req1:
        #     temp -= dec1
        #     tot += 1
        temp -= temp % dec1
        tot += temp % dec1
        if req1 > req2:
            while temp >= req2:
                temp -= dec2
                tot += 1
    elif dec2 < dec1:
        if dec2 < dec1:
            while temp >= req2:
                temp -= dec2
                tot += 1
            if req2 > req1:
                while temp >= req1:
                    temp -= dec1
                    tot += 1
    else:
        if req1 > req2:
            while temp >= req2:
                temp -= dec2
                tot += 1
        elif req2 > req1:
            while temp >= req1:
                temp -= dec1
                tot += 1
        else:
            while temp >= req1:
                temp -= dec1
                tot += 1
    output.append(tot)

for item in output:
    print(item)