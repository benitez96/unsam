def pascal(n, k):

    if n == k or k == 0:
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

