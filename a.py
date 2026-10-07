[x1, y1] = list(map(int, input().split()))
[x2, y2] = list(map(int, input().split()))

r = 0
if (x1[0] >= x2[0] and x1[0] <= x2[1]) and (y1[0] >= y2[0] and y2[0] <= y2[1]):
    print(1)
else:
    print(0)



    