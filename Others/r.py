def mystery(n, m):
    if n == 0:
        return 0
    if n == 1:
        return m
    return m + mystery(n-1,m)

print(mystery(3,6))

