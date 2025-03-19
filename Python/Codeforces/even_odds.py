"""Will be given n as an integer
Need to find all odd numbers from 1 to n and add it to a list
Need to find all even numbers and add it to the same list
k will be spaced on the same line after n
i have to find the kth term on the list
In the first sample Volodya's sequence will look like this: {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}.
The third place in the sequence is therefore occupied by the number 5.
"""

n,k = map(int, input().split())
output_list = []
#10 , 7
#1, 3, 5, 7, 9, 2, 4, 6, 8, 10
mid = n // 2
if k > mid:
    #even
    print(2*(k-mid))
else:
    print((k*2)-1)
