#https://codeforces.com/contest/1808/problem/B
"""Create two variables where we add each index of each list, sum it and do this for each of the cards"""

tests = int(input())
index = 0
total = 0
num_list = []
for i in range(tests):
    cards, numbers = map(int, input().split())
    for card in range(cards):
        list1 = list(map(int, input().split()))
        num_list.append(list1)
    for _ in range(numbers):
        for item in num_list:
            total += item[index]
            total = abs(total)
        index += 1

#too many for loops and very confused