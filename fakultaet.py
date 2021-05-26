x = 5

def fakultaet(x):
    """Berechnet die Fakultät einer Zahl.
    
    Multipliziert eine Zahl mit mit ihren Vorgängern."""
    print(x)
    while x > 1:
        return x * fakultaet(x - 1)
    else:
        return 1

print("Fakultaet ist", fakultaet(x))