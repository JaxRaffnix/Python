a = 3
n = 2
b = 3

def uparrow(a, n, b):
    print(a, n, b)
    if n == 1:
        return pow(a, b)
    else:
        while b >0:
            return uparrow(a, n - 1, uparrow(a, n, b - 1))
        else:
            return 1

print("UpArrow ist",uparrow(a, n, b))