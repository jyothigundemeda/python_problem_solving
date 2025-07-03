for i in range(5):
    print(i)

#break
print("using break")

for i in range(1, 10):
    if i == 3:
        break
    print(i)

#continue
print("using continue")

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

#list
print("using list")

list = [1, 2, 3, 4]
for i in list:
    print(i)

list = ["apple", "mango", "cherry"]
for i in list:
    print(i)

list = [1,2, 3,4]
for i in list:
    if i%2 == 0:
        print(i)



