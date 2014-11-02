

def gcd(u, v):
    return not v and u or gcd(v, u % v)

u, v = (12, 8)
print(gcd(u, v))
