# LearnPython
This is Tutorial of Python with examples and detail.


# print("Qasim Bhalli")
# if (user_input := input("Enter a number: ")) and user_input.isdigit():
#     print(f"user_input =  {user_input}")
# else:
#     print("Invalid input. Please enter a valid number.")


# seq=range(10)
# print(type(seq))

# for i in seq:
#     print(i)


# for i in range(1,10,2):
#     print(i)

# n=int(input("Enter The Number: "))
# print(n)
# for i in range(1,11):
#     print(i*n)

# n=int(input("enter the number: "))
# sum=0
# i=1
# # for i in range(1,n+1):
# #     # print(i)
# #     sum+=i
    
# # print(sum)    

# while i<=n:
#     print(i)
#     i+=1
#     sum+=i

# list_1="hello"

# print(list_1.join("world"))

empty_string = "Test" * 0
print(f"Empty string: '{empty_string}'")
print(len(empty_string))
print(5==5.0)
print(bool(-10))
print(bool([""]))
print(bool())


lst: list = [("name", 34)]
d = dict(lst)       # skipped type hint to see what data type is assigned at runtime
print(d, type(d))

num: int = 5
comp = complex(num)   # skipped type hint to see what data type is assigned at runtime
print(comp, type(comp))  # Output: (5+0j)

person={"name":"Qasim","age":25}
person.clear()
print("After: person.clear() = ", person)  # Output: {}
print("After: person.clear() = ", len(person))  # Output: {}


# F = (C * 9/5) + 32
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = {str(c)+"c":  str((c * 9/5) + 32)+"f" for c in celsius_temps}
print(fahrenheit_temps)  # Output: {0: 32, 10: 50, 20: 68, 30: 86, 40: 104}

unknown: set = {} # dectionary
print("type(unknown)     = ", type(unknown))
unknown: set = {""} # set
print("type(unknown)     = ", type(unknown))


my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}

# sorted_dict =my_dict.keys+":"+sorted(my_dict.values())
# print(sorted_dict)


def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()


print(gen)

print(gen, " : ", type(gen))

# Iterate over the generator
for value in gen:
    print(value, " : ", type(value))
    
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(0))  # Output: 120    