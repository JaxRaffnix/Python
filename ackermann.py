n = int(input("n ist:"))
m = int(input("m ist:"))

def ack(x, y):
    # print(x, y)
    while x > 0:
        if y == 0:
            return ack(x - 1 ,1)
        else:
            return ack(x - 1, ack(x, y - 1))
    else:
        return y + 1
        
print("AckermannZahl für", n, m, "ist:", ack(n, m))