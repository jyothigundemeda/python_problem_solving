# ip = 8
#op = 2 4 6 8
# ip2 = -5
# op2 = -2 -4 -6 -8
n = int(input())
if n > 0:
    i = 2
    while i <= n :
        if i%2 == 0:
            print(i)
        i += 1
else:
    i = -2
    while i >= n:
        if i%2 == 0:
            print(i)
        i -= 1

''' ip = 5
op = 1 2 3 4 5'''


n = int(input())
if n > 0:
    i = 1 
    while i <= n:
        print(i)
        i += 1
else:
    print("negative")


''' ip = 5
    op = 2 3 4 6 6 9 12 10 15'''

n = int(input())
if n > 0:
    i = 1 
    while i<=n:
        print(i*2, i*3, end=' ')
        i += 1
else:
    print("negative ")



'''negative table'''

n = int(input())
i = 1
while i<= 10:
    print(n, "*", i, "=", n*i)
    i += 1


#convert negative to positive without abs
n = int(input())
if n<0:
    n = -n
    print(n)

#sum of input number
n = int(input())
sum = 0
i = 1
while i <= n:
    a = n%10
    sum += a
    n = n//10
print(sum)
i += 1 

#2nd way
n = int(input())
n = n.lstrip('-')
digits = [int(d) for d in n]
total = sum(digits)
print(total)
