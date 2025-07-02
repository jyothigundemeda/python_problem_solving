x = 10
if x > 5:
    print("true")

#check positve or negative
n = int(input("enter number:"))
if n > 0:
    print("postive")


#check number divisible with 3 and 5
n = int(input("enter a number:"))
if n%3 == 0 and n%5 == 0 :
    print("divisible by both 3 and 5")
else:
    print("not divisible by 3 and 5")


#number divisible by 2 and 8

n = int(input("enter a number:"))
if n%2 == 0 and n%8 == 0:
    print("divisible by both 2 and 8")
else:
    print("not divisible ")


#if else (basic)
x = int(input("enter a number:"))
if x>5:
    print("x is greater than 5")
else:
    print("x is lesser than 5")

#even or odd
n = int(input("enter number:"))
if n%2 == 0:
    print("even")
else:
    print("odd")
    
# positive negative 
n = int(input("enter a number"))
if n < 0:
    print("-ve")
else:
    print("+ve")

# eligible for vote or not
age = int(input("enter age:"))
if age < 18:
    print("not eligible")
else:
    print("eligible")

#find largest of two numbers
a = int(input("enter a:"))
b = int(input("enter b:"))
if a>b:
    print("a is largest")
else:
    print("b is largest")

#passord checking
a = input("enter letter:")
vowels = 'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'
if a == vowels:
    print("vowels")
else:
    print("consonent")

#checking password 
password = 'kiet'
n = input("enter password:")
if n == password:
    print("valid")
else:
    print("not valid")

#leap year
n = int(input("enter year"))
if n%4 == 0 or n%400 == 0 or n%100 != 0:
    print("leap year")
else:
    print("not leap")
