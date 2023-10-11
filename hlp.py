'''Given a sequence of integers and an integer S, output the minimal length of the subsequence of 
consecutive elements of the sequence, the sum of which is greater than or equal a subsequence, output 0.

Input:

sequence of integers on the first line, separated by space

S on the second line'''

def min_subsequence_length(arr, Summ):
    x = len(arr)
    min_length = float()

    for i in range(x):
        current_sum = 0
        for j in range(i, x):
            current_sum += arr[j]
            if current_sum >= Summ:
                min_length = min(min_length, j - i + 1)

    return min_length if min_length != float() else 0
arr = list(map(int, input().split()))
Summ = int(input())
result = min_subsequence_length(arr, Summ)
print(result)
