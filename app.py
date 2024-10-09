# Variables
age = 20
price = 19.95
first_name = 'Pierre'
is_online = True
print(age)


# Most Replayed
name = input('What is your name?')
print("Hello" + name)

#Types Conversion :
birth_year = input('Enter your birth year?')
age = 2024 - int(birth_year)
print(age)

#Exo
first = float(input("First"))
second = float(input("Second"))
sum = first + second
print("Sum" + str(sum))

# Strings
course = "Python for Beginners"
print(course.upper()) # conversion min -> maj
print(course.lower()) # conversion maj -> min
print(course.find("y")) # position first "y"
print(course.replace("for", '4')) # replace
print("Python" in course)

# Arithmetic Operators
print (10%3)
x = 10
x = x + 3
x *= 3
print(x)

# Logical Operator
price_two = 25
print(not price_two > 10 ) #not / or / and

# if Statements
temperature = 35

if temperature > 30:
    print("It's a hot day !")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print('Done')

# While Loops
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1

#Lists
names = ["John", "Bob", "Pierre", "Mary"]
names[0] = "Jon"
print(names[0:3])

# Lists Methods
numbers = [1,2,3,4,5]
numbers.insert(0, -1)
numbers.remove(4)
print(1 in numbers)
print(numbers)


