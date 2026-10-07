n = int(input())
a = [int(x) for x in input().split()]
print(a)

arr = []
count = 0
for i in range(n):
    count = 0
    for j in range(i, n):
           
        if(a[i] > a[j]):
            count += 1
            
        if a[i] == max(a):
            count = 0
            break 
            
        if(a[i] < a[j]):
            count += 1
            print('Br')
            break
        
    if(count != n):
        arr.append(count)
    else:
        arr.append(0)
print(*arr)    

        