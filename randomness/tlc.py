

def rand(a=0):
    i = 0
    while i <= 19:
        a = (385934821 * a + 1) % (2 ** 32)
        i += 1
        print(a)

rand(0)
