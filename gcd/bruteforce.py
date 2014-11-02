

def gcd(u, v):
    d = min(u, v)
    while u % d or v % d:
        d -= 1
    return d

u, v = (12, 8)
print(gcd(u, v))
