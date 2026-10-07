x = list(map(int, input().split()))
y = list(map(int, input().split()))

xMin = min(x)
xMax = max(x)

yMin = min(y)
yMax = max(y)

r = 0

if (xMax >= yMin and xMax <= yMax) or (yMax >= xMin and yMax <= xMax):
    r = 1

print(r)
    
    