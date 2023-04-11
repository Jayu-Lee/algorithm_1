def QuickSelect(L, k):
    if len(L) == 1:
        return L[0]
    
    p = L[0]
    S = [n for n in L if n < p]
    M = [n for n in L if n == p]
    L = [n for n in L if n > p]

    if k < len(S):
        return QuickSelect(S, k)
    elif k < len(S) + len(M):
        return p
    else:
        return QuickSelect(L, k - len(S) - len(M))
    
n, k = map(int, input().split())
L = list(map(int, input().split()))

print(QuickSelect(L, k-1))