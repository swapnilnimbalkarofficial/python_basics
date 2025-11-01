# print("Hello, World!")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum:", a + b)


#Swap Two Variables
# a, b = 5, 10
# a, b = b, a
# print(a, b)

# Find Square of a Number
# num = int(input("Enter number: "))
# print("Square:", num ** 2)

# Find Cube of a Number
# num = int(input("Enter number: "))
# print("Cube:", num ** 3)

# Check Even or Odd
# num = int(input("Enter number: "))
# print("Even" if num % 2 == 0 else "Odd")

# Check Positive, Negative or Zero
# num = int(input("Enter number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# Find Maximum of Two Numbers
# a = int(input("Enter first: "))
# b = int(input("Enter second: "))
# print("Max:", max(a, b))

# Find Maximum of Three Numbers
# a = int(input())
# b = int(input())
# c = int(input())
# print("Max:", max(a, b, c))

# Simple Calculator
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# op = input("Enter operator (+,-,*,/): ")

# if op == '+': print(a + b)
# elif op == '-': print(a - b)
# elif op == '*': print(a * b)
# elif op == '/': print(a / b)
# else: print("Invalid operator")

# Loops and Conditions
# 11️⃣ Print First 10 Natural Numbers
# for i in range(1, 11):
#     print(i)

# Print Sum of First N Natural Numbers
# n = int(input("Enter N: "))
# s = sum(range(1, n + 1))
# print("Sum:", s)


# Print Multiplication Table
# n = int(input("Enter number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")


# Factorial of a Number
# n = int(input("Enter number: "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("Factorial:", fact)


# Fibonacci Series up to N terms
# n = int(input("Enter terms: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Check Prime Number
# n = int(input("Enter number: "))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")


# Reverse a Number
# n = int(input("Enter number: "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# print("Reversed:", rev)


# Sum of Digits of a Number
# n = int(input("Enter number: "))
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print("Sum of digits:", s)

# Check Palindrome Number
# n = input("Enter number: ")
# print("Palindrome" if n == n[::-1] else "Not Palindrome")


# Armstrong Number
# n = int(input("Enter number: "))
# num = n
# s = 0
# while n > 0:
#     d = n % 10
#     s += d ** 3
#     n //= 10
# print("Armstrong" if s == num else "Not Armstrong")

# Find Largest Element in a List
# nums = [3, 7, 2, 9, 5]
# print("Largest:", max(nums))

# Find Smallest Element in a List
# nums = [3, 7, 2, 9, 5]
# print("Smallest:", min(nums))

# Sum of List Elements
# nums = [1, 2, 3, 4, 5]
# print("Sum:", sum(nums))

# Reverse a List
# nums = [1, 2, 3, 4, 5]
# print("Reversed:", nums[::-1])

# Remove Duplicates from List
# nums = [1, 2, 2, 3, 3, 4]
# unique = list(set(nums))
# print(unique)

# Sort a List
# nums = [5, 2, 9, 1]
# nums.sort()
# print(nums)

# String Palindrome
# s = input("Enter string: ")
# print("Palindrome" if s == s[::-1] else "Not Palindrome")

# Count Vowels in a String
# s = input("Enter string: ").lower()
# vowels = "aeiou"
# count = sum(1 for ch in s if ch in vowels)
# print("Vowel count:", count)

# Count Words in a Sentence
# s = input("Enter sentence: ")
# print("Words:", len(s.split()))

# Pattern Programs
# 31️⃣ Right Triangle Star Pattern
# n = int(input("Enter rows: "))
# for i in range(1, n+1):
#     print("*" * i)

# Floyd’s Triangle
# n = int(input("Enter rows: "))
# num = 1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

#Functions and Logic
#Factorial Using Function
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n-1)

# print(factorial(2))

# Prime Check Using Function
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))

# Fibonacci Using Recursion
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# for i in range(10):
#     print(fib(i), end=" ")


# Find GCD of Two Numbers
# import math
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("GCD:", math.gcd(a, b))

# Find LCM of Two Numbers
# import math
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("LCM:", abs(a*b)//math.gcd(a, b))

# Reverse a String
# s = input("Enter string: ")
# print(s[::-1])


# Check Leap Year
# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# Sum of Even Numbers in a List
# nums = [1, 2, 3, 4, 5, 6]
# print(sum([x for x in nums if x % 2 == 0]))

# Count Digits in Number
# n = int(input("Enter number: "))
# count = len(str(n))
# print("Digits:", count)

# Convert Celsius to Fahrenheit
# c = float(input("Enter Celsius: "))
# f = (c * 9/5) + 32
# print("Fahrenheit:", f)

# Convert Kilometers to Miles
# km = float(input("Enter kilometers: "))
# miles = km * 0.621371
# print("Miles:", miles)

# Simple Interest
# p = float(input("Principal: "))
# r = float(input("Rate: "))
# t = float(input("Time: "))
# si = (p * r * t) / 100
# print("Simple Interest:", si)


# Compound Interest
# p = float(input("Principal: "))
# r = float(input("Rate: "))
# t = float(input("Time: "))
# ci = p * ((1 + r/100)**t - 1)
# print("Compound Interest:", ci)

# Find ASCII Value of Character
# ch = input("Enter character: ")
# print("ASCII value:", ord(ch))

# Count Uppercase and Lowercase Letters
s = input("Enter string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase:", upper, "Lowercase:", lower)