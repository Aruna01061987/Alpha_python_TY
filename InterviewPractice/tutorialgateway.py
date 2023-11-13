#WAP to check if a substring is present in a string

# class substring:
#
#     def read_string(x,y):
#         if x in y:
#             print("yes")
#         else:
#             print("no")

#a = substring
#x = str(input("Enter the substring:"))
#y = str(input("enter the string:"))
#a.read_string(x,y)

# class s_string(substring):
#     def read_string(x,y):

# b = s_string
#
# c = str(input("Enter the substring:"))
# d = str(input("enter the string:"))
# b.read_string(c,d)

#************************************************************

#WAP to print the second largest number in among 3 numbers;

# l_num = []
# n = int(input("enter  the number of elements: "))
#
# for i in range(1,n+1):
#     num = int(input(f"enter the {i} number: "))
#     l_num.append(num)
# print(l_num)
# print(f"The second largest number is : ", sorted(l_num)[1])

#************************************************************

# WAP to print calender

# import calendar
#
# month = int(input("enter the month: "))
# year = int(input("enter the year: "))
# print(calendar.month(year, month))
# print(calendar.monthcalendar(year, month))

#WAP to find fibonacci series
#
# number = int(input("enter the number: "))
# first = 0
# second = 1
# sum = 0
#
# for i in range(0, number):
#     print(first, end=' ')
#     sum = sum + first
#     first = second
#     second = second + i


# num = int(input("enter the number: "))
# n1 = 0
# n2 = 1
# for i in range(0, num):
#     print(n1, " ")
#     n1 = n2
#     n2 = n2 + i

#WAP to find if the number is a prime number

# num = int(input("enter the number: "))
# flag = 0
# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break
#
# if flag == 1:
#     print(" the number is not prime")
# else:
#     print(" the  number is a  prime number")

# def prime_number(num):
#     flag = 0
#     for i in range(2, num):
#         if num % i == 0:
#             flag = 1
#             break
#
#     if flag == 1:
#         print(" the number is not prime")
#     else:
#         print(" the  number is a  prime number")
#
#
# num = int(input("enter the number: "))
# prime_number(num)

#WAP to print multiplication table of a given number using .format
import datetime
#
# n = int(input("enter the number: "))
# for i in range(1,11):
#     # print("{} * {} = {}".format(n, i, n * i))
#
#     print(f"{n} * {i} = {n * i}")

#WAP Python Program to Get Current Date and Time

# from datetime import date
# from datetime import datetime
#
# date = date.today()
# print("{} is the date today".format(date))
# time_now = datetime.now()
# print(f"the time now is {time_now} ")

# #WAP to create a simple calculator

#WAP to find sum of natural numbers

# num = int(input("enter the number: "))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print("sum of natural numbers is {}".format(sum))

#WAP to find sum of even numbers

# num = int(input("enter the number:  "))
# sum = 0
# for n in range(2, num+1):
#     if n % 2 == 0:
#         sum += n
# print("sum: ", sum)
# print("avg =", sum/num)

#Python Program to Count Number of Digits in a Number

# num = int(input(" Enter the number: "))
# count = 0
# while(num > 0):
#     num = num // 10
#     count += 1
# print("The number of digits are: ", count)

# def no_digit(num):
#     count = 0
#     while (num > 0):
#         num = num // 10
#         count += 1
#     print("The number of digits are: ", count)
#
# num = int(input(" Enter the number: "))
# no_digit(num)

#WAP to print fibonacci series using while loop:
# num = int(input("enter the number: "))
# num1 = 0
# num2 = 1
# i = 0
# sum =0
# while (i < num):
#     print(num1)
#     sum = sum + num1
#     next = num1 + num2
#     num1 = num2
#     num2 = next
#     i += 1

#WAP to print factors of a number

# num = int(input("enter the number: "))
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)

#WAP to find factorial of a number

# num = int(input("enter the number: "))
# sum = 1
# for i in range(num, 1, -1):
#     sum = sum * i
# print(sum)

#WAP to find the number of digits in a no

num = int(input("enter the number: "))
count = 0
while(num > 0):
    num = num // 10
    count += 1
print("number of digits is:", count)












