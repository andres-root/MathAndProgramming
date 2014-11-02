

def rand(a=0):
    a = (385934821 * a + 1) % (2 ** 32)
    return a

print(rand())
