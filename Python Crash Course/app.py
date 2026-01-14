print("Hello, World!")
x=10
y=20
sum = x + y
print("Sum of", x, "and", y, "is", sum)

word = "Python"
print("The word is:", word)
length = len(word)
print("Length of the word is:", length)
print( word[0], word[1], word[2], word[3], word[4], word[5])

print(word[-1])

print(word[2:4])
print("har\\itha\'sfsf\'fsfs")


newname = "   haritha Mihimal fgdfgd gdfg"
print(newname.upper())
print(newname.title())
print(newname.lower())
print(newname.rstrip())
print(newname.lstrip())
print(newname.find("Mihimal"))
print(newname.replace("haritha", "kumar"))
print("haritha" in newname) 

# operators
print("operators")
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# ogmented operatoers
print("ogmented operators")
print(a)
a += 5
print(a)
a *= 2
print(a)
a -= 10
print(a)
a /= 3
print(a)
a //= 2
print(a)
a %= 4
print(a)


# round
print("round function")
num = 5.6789
print(round(num))
print(round(num, 1))
print(round(num, 2))
print(round(num, 3))

# abs
print("absolute value")
num2 = -10
print(abs(num2))


import math
print("math module functions")
print(math.ceil(4.2))
print(math.floor(4.7))
print(math.sqrt(16))

# input
# name = input("Enter your name: ")
# print("Hello,", name)

# age = int(input("Enter your age: "))
# print("You are", age, "years old.")

# type conversion
print(bool("Hello"))

# character to unicode and vice versa
print(chr(97))
print(chr(65))
print(ord('a'))
print(ord('A'))
print(ord('a')-ord('A'))

# conditional statements
print("conditional statements")
if (10>15):
    
    print("10 is greater than 15")
elif (10 == 15):
    print("10 is equal to 15")
else: print("10 is not greater than 15")

# ternary operator
print("ternary operator")
age=12
messge = "Eligible" if age >= 18 else "Not Eligible"
print(messge)

length = 11
breadth = 10
area = length * breadth if length >=0 and breadth >=0 else "Invalid dimensions"
print("Area is:", area)

if 10 <= length <= 20:
    print("Length is between 10 and 20")
    
print("bag">"apple")
print("cat"<"dog")
print("bag">"cat")
print("bag"<"Bag")


# for loop
print("for loop")
for i in range(10):
    print(i, end=" ")
    
print()
for i in range(1,20,2):
    print(" "* (10 - i//2) + "*" * i)
    
    
print("Nested loop with f-string")
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
        
print("Nested loop without f-string")
for x in range(5):
    for y in range(3):
        print("("+str(x)+"," + str(y)+")")
        
i=0  
j=0    
while True:
    if i<10:
        if i%2==0 and i!=0:
            j+=1
            print(i)
            
    i+=1
    if i>=10:
        print(f"we have {j} even numbers")
        break
        