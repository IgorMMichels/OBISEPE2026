N = int(input())

a, b, c, d, e, f, g = map(int, input().split())

a = a - d - e

b = b - d - f

c = c - e - f

N = N - g - (a + b + c + d + e + f)

if N < 0:   
    print("S")
else:
    print("N")