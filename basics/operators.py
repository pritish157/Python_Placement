# # Try these 10 questions:

# # Take two numbers from user and swap them using + and - (without 3rd variable).
# a = int(input("enter num.1 : "))
# b = int(input("enter num.2 : "))
# a = a+b
# b = a-b
# a = a-b
# print(a,b)
# # Swap two numbers without third variable


# print("Before swap: a =", a, ", b =", b)
# # Method 2: Using XOR (bitwise)

# a = a ^ b   # a = 5 ^ 10
# b = a ^ b   # b = (5 ^ 10) ^ 10 = 5
# a = a ^ b   # a = (5 ^ 10) ^ 5 = 10

# print("After swap (Method 2): a =", a, ", b =", b)

# # Method 3: Python shortcut
# a, b = b, a
# print("After swap (Method 3): a =", a, ", b =", b)

# Take a number and check if it’s odd/even using bitwise &.
# a = int(input("enter a number"))
# if(a & 1 ==0):
#     print("even")
# else:
#     print("odd")


# Write a program to check if two numbers are equal using is vs ==. Explain difference.
# a = int(1000) 
# b = int(1000)
# c = "pritish"
# d = "pritish"
# e = "pri"+"tish"
# print(type(a))
# print(a is b)
# print(a==b)
# print(c==d==e)
# print(c is not e)
# print(c is d)
# Take a number and print its binary representation using bitwise operators.


# Write code to find if n is a power of 2 using bitwise.

# Take two numbers and compute GCD using bitwise operations (hint: use a & b trick).

# Find whether a character is vowel/consonant using membership operators (in).

# Check if a given number is in a list using membership operators.

# Take a number and perform left shift <<1 and right shift >>1. Explain the result.

# Difference between is and == with examples in lists and integers.