#need my own function for gcd and lcm because math module is not allowed
def gcd(a, b):
    while b != 0:
        a = b
        b = a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

cookie_no1, cookie_no2, target = map(int, input().split())
zero_values = []
if cookie_no1 > cookie_no2:
    largest = cookie_no1
    smaller = cookie_no2
#account for equal cases later
else:
    largest = cookie_no2
    smaller = cookie_no1

close_rem, far_rem = target % largest, target % smaller
high_rem_far, high_rem_close = (((target // largest) + 1) * largest) - target, (((target // smaller) + 1) * largest) - target
if close_rem == 0:
    zero_values.append(target / largest)
if far_rem == 0:
    zero_values.append(target / smaller)

#trying to make cases like (2 3 10) work
minus_lcm = target - lcm(cookie_no1, cookie_no2)
if minus_lcm % cookie_no1 == 0:
    print("0 " + str(int(lcm(cookie_no1, cookie_no2) / largest + minus_lcm / cookie_no1)))
elif minus_lcm % cookie_no2 == 0:
    print("0 " + str(int(lcm(cookie_no1, cookie_no2) / largest + minus_lcm / cookie_no2)))
else:
    if len(zero_values) > 0:
        for item in zero_values:
            print(item)
    elif close_rem > high_rem_close:
        print(str(high_rem_close), str(target // smaller + 1))
    elif close_rem < high_rem_close:
        print(str(close_rem), str(target // largest))
    elif far_rem > high_rem_far:
        print(str(high_rem_far), str(target // largest + 1))
    elif far_rem < high_rem_far:
        print(str(far_rem), str(target // smaller))