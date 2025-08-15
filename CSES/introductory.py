def weid_algorithm():
    n = int(input())
    final = ""
    final += str(n)
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = int(n * 3 + 1)
        final += " " + str(n)
    print(final)

def missing_number():
    n = int(input())
    nums = list(map(int, input().split()))
    total = 0
    for i in range(1, n+1): total += i
    print(total - sum(nums))

def repetitions():
    s = input()
    cur = 'A'
    count = 0
    counts = []
    for char in s:
        if char == cur:
            count += 1
            counts.append(count)
        else:
            cur = char
            count = 1
            counts.append(count)
    print(max(counts))

def increasing():
    n = int(input())
    nums = list(map(int, input().split()))
    total = 0
    for i in range(1,n+1):
        if i != n:
            if nums[i] < nums[i-1]:
                total += nums[i-1] - nums[i]
                nums[i] += nums[i-1] - nums[i]
        else:
            if nums[i-1] < nums[i-2]:
                total += nums[i-2] - nums[1]
                nums[i] += nums[i-2] - nums[i-1]
    print(total)

def permutations():
    n = int(input())
    final = ""
    if n == 1:
        print(1)
    elif n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        firstNums = [str(i) for i in range(1, n+1, 2)]
        firstNums.reverse()
        otherNums = [str(i) for i in range(2, n+1, 2)]
        otherNums.reverse()
        final += " ".join(firstNums) + " "
        final += " ".join(otherNums)
        print(final)

def num_spiral():
    pass

num_spiral()