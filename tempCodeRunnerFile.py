def min_subsequence_length(sequence, S):
    n = len(sequence)
    min_length = float('inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += sequence[j]
            if current_sum >= S:
                min_length = min(min_length, j - i + 1)

    return min_length if min_length != float('inf') else 0