C, P, F = map(int, input().split())

n = P - (C * F) 

if (n >= 0):
    print("S")
else:
    print("N")