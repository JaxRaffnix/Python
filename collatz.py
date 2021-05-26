n = int(input("CollatzZahl:"))

def collatz(n):
    print(n)
    while n > 1:
        if n % 2:
            return 1 + collatz((3 * n) + 1)
        else:
            return 1 + collatz(n / 2)
    else:
        return 0

print("CollatzZahl ist", collatz(n))