
N = int(input())

a = [int(x) for x in input().split()]

max = max(a)
count = 0
index = -1;
for i in range(N):
    if a[i] == max and i != index:
        print(a[i])
        count += 1
        index = i

if count >= 2:
    print("S")
else:
    print("N")