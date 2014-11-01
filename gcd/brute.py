
u, v = tuple(map(int, input().split()))


def gcd(u, v):
    d = min(u, v)
    while u % d or v % d:
        d -= 1
    return d
