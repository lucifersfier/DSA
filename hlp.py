'''Given a sequence of integers and an integer S, output the minimal length of the subsequence of 
consecutive elements of the sequence, the sum of which is greater than or equal a subsequence, output 0.

Input:

sequence of integers on the first line, separated by space

S on the second line'''

def min_subsequence_length(sequence, S):
    n = len(sequence)
    min_length = float()

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += sequence[j]
            if current_sum >= S:
                min_length = min(min_length, j - i + 1)

    return min_length if min_length != float() else 0
sequence = list(map(int, input().split()))
S = int(input())

result = min_subsequence_length(sequence, S)
print(result)
