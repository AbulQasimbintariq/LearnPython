# # class order_detail:
# #     def __init__(self,product,checkout):
# #         self.product=product
# #         self.checkout=checkout
        
# #     def checkID(self):
# #         print("Its is product")  
# #     def ordered(self):
# #         print("Order is checkout")      
     
# # step1=order_detail("apple")  
# # checkID.step1()     


# # x: int= 5
# # y: int= ~x
# # print("y = ", y, type(y),bin(x),type(bin(x)),type(x))
 
 
# # x: int = 5  # Binary: 0101
# # y: int = ~x  # y is now -6 (binary: 1010, but in two's complement form)
# # print("y = ", y)


# def calculator():
#       """
#   A calculator function that takes user input for numbers and operations,
#   including modulus, floor division, and exponentiation.
#   """
# while True:
#     operation = input("Enter the operation (+, -, *, /, %, //, ** or 'q' to quit): ")
#     if operation.lower() == 'q':
#       break
#     if operation not in ('+', '-', '*', '/', '%', '//', '**'):
#       print("Invalid operation.")
#       continue

#     try:
#       num1 = float(input("Enter the first number: "))
#       num2 = float(input("Enter the second number: "))
#     except ValueError:
#       print("Invalid input. Please enter numbers only.")
#       continue

#     if operation == '+':
#       result = num1 + num2
#     elif operation == '-':
#       result = num1 - num2
#     elif operation == '*':
#       result = num1 * num2
#     elif operation == '/':
#       if num2 != 0:
#         result = num1 / num2
#       else:
#         result = "Error: Division by zero."
#         print(result)
#         continue
#     elif operation == '%':
#       result = num1 % num2
#     elif operation == '//':
#       if num2 != 0:
#         result = num1 // num2
#       else:
#         result = "Error: Division by zero."
#         print(result)
#         continue
#     elif operation == '**':
#       result = num1 ** num2

#     print("Result:", result)

# calculator()

  
  
#   def grading_system(marks):
#       """
#   This function takes marks as input and returns the corresponding grade.

#   Args:
#     marks: The marks obtained by the student.

#   Returns:
#     The grade corresponding to the marks.
#   """
#   if marks >= 90:
#     grade = "A+"
#   elif marks >= 80:
#     grade = "A"
#   elif marks >= 70:
#     grade = "B"
#   elif marks >= 60:
#     grade = "C"
#   elif marks >= 50:
#     grade = "D"
#   else:
#     grade = "F"
#   return grade

# # Get marks as input from the user
# while True:
#   try:
#     marks = float(input("Enter the marks: "))
#     if 0 <= marks <= 100:
#       break
#     else:
#       print("Marks must be between 0 and 100.")
#   except ValueError:
#     print("Invalid input. Please enter a number.")

# # Determine the grade
# grade = grading_system(marks)

# # Print the grade
# print(f"The grade for {marks} marks is: {grade}")



# def check_status(code):
#     match code:
#         case 200:
#             print("OK")
#         case 400:
#             print("Bad Request")
#         case 404:
#             print("Not Found")
#         case _:
#             print("Unknown Status")

# check_status(200)  # Output: OK
# check_status(404)  # Output: Not Found
# check_status(500)  # Output: Unknown Status 


# # Multiplication table
# for outer in range(1, 6): # outer loop
#     print(f"Multiplication table for {outer}:")
#     for inner in range(1, 6): # nested inner loop
#         print(f"{outer} * {inner} = {outer * inner}")
#     print()  # Add a blank line after each row 
    
#     total: int = 0
# for i in range(1, 101):
#     total += i
# print("Sum of numbers from 1 to 100:", total)  

# num: int = 24
# factors = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         factors.append(i)
# print(f"Factors of {num}: {factors}") 

# **Projected Economy Size of AI:**

# The projected economy size of AI is significant, with estimates varying depending on the source and methodology. Here are some notable projections:

# 1. **Global AI Market Size:**
# 	* By 2025: 
# 1.5 trillion (Source: PwC)
# 2. **AI-Driven Economic Growth:**
# 	* By 2025: AI is expected to contribute 10% to global GDP growth (Source: Accenture)
# 	* By 2030: AI is expected to contribute 14% to global GDP growth (Source: PwC)
# 3. **AI-Generated Revenue:**
# 	* By 2025: AI is expected to generate 
# 33.5 trillion in revenue (Source: McKinsey)
# 4. **Job Market Impact:**
# 	* By 2025: AI is expected to create 133 million new jobs globally (Source: World Economic Forum)
# 	* By 2030: AI is expected to automate 30% of current jobs globally (Source: McKinsey)

# **Industry-Specific Projections:**

# 1. **Healthcare:**
# 	* By 2025: AI is expected to generate 
# 100 billion in revenue (Source: Accenture)
# 3. **Manufacturing:**
# 	* By 2025: AI is expected to generate 
# 20 billion in revenue (Source: MarketsandMarkets)

# **Regional Projections:**

# 1. **North America:**
# 	* By 2025: AI is expected to generate 
# 50 billion in revenue (Source: IDC)
# 3. **Asia-Pacific:**
# 	* By 2025: AI is expected to generate $200 billion in revenue (Source: MarketsandMarkets)

# Note: These projections are based on various assumptions, including the pace of AI development, adoption rates, and economic trends. The actual economy size of AI may vary depending on several factors.

# """
#  my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("Before: my_set = ", my_set)
# my_set.difference_update({1, 5, 3, 'A'})
# print("After:  my_set = ", my_set)
 
 
 
#  # prompt: generate examples of all the method of set

# # Example usage of set methods

# # Initialize two sets for demonstration
# set1: set = {1, 2, 3, 4, 5}
# set2: set = {4, 5, 6, 7, 8}

# # 1. add(): Adds an element to the set.
# set1.add(6)
# print(f"add(6): {set1}")  # Output: {1, 2, 3, 4, 5, 6}

# # 2. clear(): Removes all elements from the set.
# set_copy: set = set1.copy()
# set_copy.clear()
# print(f"clear(): {set_copy}")  # Output: set()

# # 3. copy(): Returns a copy of the set.
# set_copy: set = set1.copy()
# print(f"copy(): {set_copy}")  # Output: {1, 2, 3, 4, 5, 6}

# # 4. difference(): Returns a set containing the difference between two or more sets.
# difference_set: set = set1.difference(set2)
# print(f"difference(): {difference_set}")  # Output: {1, 2, 3}

# # 5. difference_update(): Removes the items in this set that are also included in another, specified set.
# set1.difference_update(set2)
# print(f"difference_update(): {set1}")  # Output: {1, 2, 3}
# set1: set = {1, 2, 3, 4, 5,6} #reset set1

# # 6. discard(): Remove the specified item.
# set1.discard(6)
# print(f"discard(6): {set1}")  # Output: {1, 2, 3, 4, 5}

# # 7. intersection(): Returns a set, that is the intersection of two other sets.
# intersection_set: set = set1.intersection(set2)
# print(f"intersection(): {intersection_set}")  # Output: {4, 5}

# # 8. intersection_update(): Removes the items in this set that are not present in other, specified set(s)
# set1.intersection_update(set2)
# print(f"intersection_update(): {set1}") # Output: {4, 5}
# set1 = {1, 2, 3, 4, 5,6} #reset set1

# # 9. isdisjoint(): Returns whether two sets have a intersection or not.
# print(f"isdisjoint(): {set1.isdisjoint(set2)}")  # Output: False
# print(f"isdisjoint(): {set1.isdisjoint({9,10})}") # Output: True

# # 10. issubset(): Returns whether another set contains this set or not.
# print(f"issubset(): {set1.issubset(set2)}")  # Output: False
# print(f"issubset(): {{1,2}}.issubset({set1})")  # Output: True
# print(f"issubset(): {{1,2}}.issubset({{1,2}})")  # Output: True


# # 11. issuperset(): Returns whether this set contains another set or not.
# print(f"issuperset(): {set1.issuperset(set2)}")  # Output: False
# print(f"issuperset(): {set1.issuperset({1,2})}")  # Output: True
# print(f"issuperset(): {{1,2}}.issuperset({{1,2}})")  # Output: True

# # 12. pop(): Removes a random element from the set.
# removed_element: int = set1.pop()
# print(f"pop(): {removed_element}")  # Output: (random element)
# print(f"set after pop(): {set1}")  # Output: (set without removed_element)
# set1.add(removed_element)#put back the element for others test

# # 13. remove(): Removes the specified element. Raises an error if the element is not present.
# set1.remove(1)
# print(f"remove(1): {set1}")  # Output: {2, 3, 4, 5,6}
# set1.add(1)#put back the element for others test

# # 14. symmetric_difference(): Returns a set with the symmetric differences of two sets.
# symmetric_difference_set: set = set1.symmetric_difference(set2)
# print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: {1, 2, 3, 6, 7, 8}

# # 15. symmetric_difference_update(): Inserts the symmetric differences from this set and another
# set1.symmetric_difference_update(set2)
# print(f"symmetric_difference_update(): {set1}")  # Output: {1, 2, 3, 6, 7, 8}
# set1 = {1, 2, 3, 4, 5,6} #reset set1

# # 16. union(): Returns a set containing the union of sets.
# union_set = set1.union(set2)
# print(f"union(): {union_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# # 17. update(): Update the set with the union of this set and others
# set1.update(set2)
# print(f"update(): {set1}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}

     
# add(6): {1, 2, 3, 4, 5, 6}
# clear(): set()
# copy(): {1, 2, 3, 4, 5, 6}
# difference(): {1, 2, 3}
# difference_update(): {1, 2, 3}
# discard(6): {1, 2, 3, 4, 5}
# intersection(): {4, 5}
# intersection_update(): {4, 5}
# isdisjoint(): False
# isdisjoint(): True
# issubset(): False
# issubset(): {1,2}.issubset({1, 2, 3, 4, 5, 6})
# issubset(): {1,2}.issubset({1,2})
# issuperset(): False
# issuperset(): True
# issuperset(): {1,2}.issuperset({1,2})
# pop(): 1
# set after pop(): {2, 3, 4, 5, 6}
# remove(1): {2, 3, 4, 5, 6}
# symmetric_difference(): {1, 2, 3, 7, 8}
# symmetric_difference_update(): {1, 2, 3, 7, 8}
# union(): {1, 2, 3, 4, 5, 6, 7, 8}
# update(): {1, 2, 3, 4, 5, 6, 7, 8}


# # Create some example frozensets
# frozen_set1: frozenset = frozenset([1, 2, 3, 4])
# frozen_set2: frozenset = frozenset([3, 4, 5, 6])
# frozen_set3: frozenset = frozenset([1, 2])

# print(f"frozen_set1: {frozen_set1}")
# print(f"frozen_set2: {frozen_set2}")
# print(f"frozen_set3: {frozen_set3}")
# print("\n----------\n")
# # Methods that work with frozensets (since they are immutable)
# # These methods return a new frozenset or a boolean value

# # 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
# difference_set: frozenset = frozen_set1.difference(frozen_set2)
# print(f"difference(): {difference_set}")  # Output: frozenset({1, 2})

# # 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
# intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
# print(f"intersection(): {intersection_set}")  # Output: frozenset({3, 4})

# # 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
# union_set: frozenset = frozen_set1.union(frozen_set2)
# print(f"union(): {union_set}")  # Output: frozenset({1, 2, 3, 4, 5, 6})

# # 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
# symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
# print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: frozenset({1, 2, 5, 6})

# # 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
# print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: False
# print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([7, 8]))}")  # Output: True

# # 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
# print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
# print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False

# # 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
# print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
# print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False

# # 8. copy(): Returns a new frozenset that is a shallow copy of the original.
# copy_set: frozenset = frozen_set1.copy()
# print(f"copy(): {copy_set}")  # Output: frozenset({1, 2, 3, 4})
# print(f"copy() is same object?: {copy_set is frozen_set1}") # Output: True because frozensets are immutable

     
# frozen_set1: frozenset({1, 2, 3, 4})
# frozen_set2: frozenset({3, 4, 5, 6})
# frozen_set3: frozenset({1, 2})

# ----------

# difference(): frozenset({1, 2})
# intersection(): frozenset({3, 4})
# union(): frozenset({1, 2, 3, 4, 5, 6})
# symmetric_difference(): frozenset({1, 2, 5, 6})
# isdisjoint(): False
# isdisjoint(): True
# issubset(): True
# issubset(): False
# issuperset(): True
# issuperset(): False
# copy(): frozenset({1, 2, 3, 4})
# copy() is same object?: True
    