
a = int(input(""))

x = int( a % 10)

y = int((a % 100 - x ) / 10) 

z = int((a % 1000 - x - y) / 100)


x = x ** 2
y = y ** 2
z = z ** 2

n = x + y + z

x = int(n % 10)
y = int((n % 100 - x ) / 10) 
z = int((n % 1000 - x - y) / 100)
i = int((n % 10000 - x - y - z) / 1000)


x = x ** 2
y = y ** 2
z = z ** 2
i = i ** 2 

p = x + y + z + i
print(p)
