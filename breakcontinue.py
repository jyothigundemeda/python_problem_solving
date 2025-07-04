#break is used to modify the behaviour

for i in range(10):
    if i == 5:
        break
    print(i)

#2
n = int(input())
for i in range(1, n+1):
    if i == 6:
        break
    print(i)

#continue :  skip the rest of current iteration & continue the next one

for i in range(10):
    if i == 2:
        continue
    print(i)

#ex2
while True:
    a = input("type something:")
    if a == "exit":
        break
    print("you typed:",a)

#3
while True:
    a = input("enter smtg")
    if "exit" in a:
        break
    print("you typed",a)

#skip negative numbers
n = [1, 4, -9, 7, -6, 3, -6]
for i in n:
    if i<0:
        continue
    print(i)

#stop printing chracters on space
text = "hello world"
for char in text:
    if char == 'r':
        break
    print(char, end=' ')

#skip vowels
text = "education"
vowels = "aeiou"
for char in text:
    if char in vowels:
        continue
    print(char)

#break in while
i = 1
while True:
    if i == 8:
        break
    print(i)
    i += 1

n = [10, 20, 30 ,40,50,60,]
total = 0
for i in n:
    total += 1
    if total > 100:
        break 
    print(total)