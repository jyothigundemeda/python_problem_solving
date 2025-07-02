#sum of cubes form m to n   
m = int(input("enter m:"))
n = int(input("enter n:"))
total = 0
for i in range(m, n+1):
    cube = i**3
    total += cube
print(total)


#2
d = int(input("enter distance:"))
bonus = 100
score = 0
if d>250:
        score += (d-250)*10
        d = 250
if d > 200:
        score += (d-200)*8
        d = 200
if d > 100:
        score += (d-100)*6
        d = 100
if d > 50 :
        score += (d-50)*5
        d = 50
if d > 0:
        score += d*3

score += bonus
print(score)

#7  Write a function with the name show_numbers that takes a number n and print all the numbers 
# from 0 to N with a label to identify the Even and Odd numbers as shown below
# 0 EVEN
# 1 ODD
# 2 EVEn
# 3 ODD
n = int(input("enter number:"))
for i in range (0, n+1):
       if i%2==0:
            print(i, "EVEN")
       else:
            print(i, "ODD")


#) Write a program that reads a string and prints the character of your string in reverse order.
# Sample input1:Scale
# Sample output1:
#e
#l
#a
#c
#s
n = input("enter string:")
reverse = n[::-1]
for char in reverse:
       print(char)

#You are given N numbers as input. Create a list and add the N numbers which are given as input and print the list.
#Sample input1:
#4
#1
#2
#3
#4
#Sample output1:
#[1, 2, 3, 4]
n = int(input("enter numbers:"))
numbers = []
for i in range(n):
       num = int(input())
       numbers.append(num)
print(numbers)
             
    