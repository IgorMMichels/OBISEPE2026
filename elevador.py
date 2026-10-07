E = int(input())
a, b, c = map(int, input().split())
arr = [a, b, c]
arr.sort()
l = [abs(arr[0]-E), abs(arr[1]-E), abs(arr[2]-E)]



print(arr[l.index(min(l))])

