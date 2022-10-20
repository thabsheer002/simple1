## usage logical operators
# a= 1;b=10
# print(a<b and b<30)
# print(a<b or b<30)#this expression sows how to use OR operator
# a= True
# b = False
# print(a)
# print(b)
# print(a and b)
# number = int(input("enter a number"))
# if number<20:
#     print("number is less than 20")
#     print("prog successfull")
#
# numb2 = int(input("enter a number"))
#
# if numb2>20 :
#     print("the number is greater than 20")
# else:
#     print("unsucessesfull")
a = 5;b = 6;c = 7;
# if a>b and a>c:
#     print("a is the largest number")
# elif b>c and b>a:
#     print("b is the largest number")
# else:
#     print("c may be the largest or it may be zero")
#
# for i in range(1,6,2):
#     print(i)
#     print(chr(ord('a') + i))
# for i in range(11):
#      print(i)
#      if i==3:
#           break
# print("iam out of the loop")
# else:
#     print("i have completed the for loop")
# print("execution continues")
# '''write code for printing the serier below up to n
# 2,4,8,16,32....n'''
'''nTerm = int(input("enter the nth term"))
for i in range(0,nTerm):
    if 2**i>=nTerm:
        break
    else:
        print(2**i,end=", ")'''
# ## write code for  printing the sum of series  s= 2+5+10+17..n
'''num = int(input("enter a number"))
sum = 0
for i in range(1,num):
    if i*i+1>num:
        break
    else:
        series = i*i+1
        sum = sum + series
        print(series,end="")
print()
print(sum)'''
'''functions
'''
'''in the following program we call a function using the concept pass by reference'''
# def update(x):
    # x = 10
    # print(id(x))
    # print("the value of x is : ",x)
a = 10
'''both a and x have same id since the value of both are same while if we change value of any one the id too changes'''
# print("id of a",id(a))
# update(a)
# print("vale of a : ",a)
##pattern no 1
'''A 
B C 
D E F 
G H I J 
K L M N O '''
# n = 5
# ch = 0
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print(chr(ch+65)+" ",end="")
#         ch += 1
#     print()
'''pattern 2
    *
   **
  ***
 ****
'''

# for x in range(0,5):
#     for y in range(5,x ,-1):
#         print(" ",end="")
#     for z in range (0,x):
#         print(chr(97+z),end="")
#     print()

# name1 = "amar"
# name2 = "nadh"
# print(name1+" "+name2)
# print(5*name1)
# print(4*name2)
# print(3*name2)
# n = 5
# for i in range(1,n):
#     print(i*"*")
''''*****
****
***
**
*

num = int(input("enter the limit"))
for i in range(num,0,-1):
    print(i*"*")
'''
# n = 4
# for i in range(1,n):
#     print(i*"*")
# for y in range(n,0,-1):
#     print(y*"*")
'''KKKKKKKKKK
 JJJJJJJJJ
  IIIIIIII
   HHHHHHH
    GGGGGG
     FFFFF
      EEEE
       DDD
        CC
         B

num = int(input("enter the limit"))
chAr = 65 + num
for x in range(0 , num):
     print((x)*" "+(num-x)*chr(chAr-x))
'''
# chAr=65
# print(chr(65))
# print(ord(chAr))
# num = int(input("enter the limit"))
# for i in range(0,num):
#     print(i*chr(chAr+i))
# for i in range (0,num):
#     print((num-i)*chr(chAr+i))
# pattern 35:
'''1
22
333
4444
num = 5
for i in range(0,num):
    for j in range(0,i):
        print(i,end="")
    print()'''
'''
1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
    '''
'''
pattern 37
4
33
222
1111
for i in  range(0,5):
    for j in range(0,i):
        print(5-i,end="")
    print()
'''
'''
5
54
543
5432
for i in range (0,5):
    for j in range(5,5-i,-1):
        print(j,end="")
    print()
    '''
'''how to open a file python'''
# import os
# file = input("enter the file to be opened")
# if "d"in file or "D"in file
#     os.startfile("D:")
# elsif "c"in file or "C"in file :
#     os.startfile("C:")
P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To swap the value of two variables
# we will user third variable which is a temporary variable
temp_1  P
P = Q
Q = temp_1

print("The Value of P after swapping: ", P)
print("The Value of Q after swapping: ", Q