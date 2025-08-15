n = int(input())
word = input() * 2
possibilities = []

smallest = min(word)
for i in range(n):
    if word[i] == smallest:
        possibilities.append(word[i:i+n])

possibilities.sort()
print(possibilities[0])