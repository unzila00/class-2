#arithmatic operator
a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
print("a % b  = ", a % b)   # 1 Modulus (remainder)
print("a % b  = ", a ** b)  # 1000 Exponentiation (10 * 10 * 10)
     
     #assignment operator
     x = 5
print("Assignment: x = 5                    ",x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ",x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ",x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ",x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ",x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ",x)  # Output: 1.0

#comparison operator
x: int = 10
y: int = 5

print("x == y = ", x == y)  # False, Equal
print("x != y = ", x != y)  # True, Not equal
print("x > y  = ", x > y)   # True, Greater than
print("x < y  = ", x < y)   # False, Less than
print("x >= y = ", x >= y)  # True, Greater than or equal
print("x <= y = ", x <= y)  # False, Less than or equal

#logical operator
x: bool = True
y: bool = False

print("x and y = ", x and y)  # False
print("x or y  = ", x or y)   # True
print("not x   = ", not x)    # False

#identity operator\
a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

print('\n-----\n') # seperator for better output readability

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))

#membership operator
my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  # True

print("\n-----\n")

my_string: str = "Operation Badar"

print("my_string                 = ", my_string)                # Operation Badar
print("'O' in my_string          = ", 'O' in my_string)         # True
print("'Hello' not in my_string  = ", 'Hello' not in my_string) # True
     
