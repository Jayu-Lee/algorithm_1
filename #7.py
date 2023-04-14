#최대 구간 합 (분할정복)

def max_sum(A, left, right):
    if left == right:
        return A[left]
    
    m = (left + right) // 2
    left_sum = max_sum(A, left, m)
    right_sum = max_sum(A, m+1, right)
    
    max_left = A[m]
    total_sum = max_left
    for i in range(m-1, left-1, -1):
        total_sum += A[i]
        max_left = max(max_left, total_sum)
        
    max_right = A[m+1]
    total_sum = max_right
    for i in range(m+2, right+1):
        total_sum += A[i]
        max_right = max(max_right, total_sum)
        
    return max(left_sum, right_sum, max_left + max_right)

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)