#  #  Python Start

# print("Hello Qasim")


# # VARIAABLES WITH DIFFERENT DATA TYPE

# name="Qasim"                # string
# floot=12.12                 # Float
# num=12                      # integer
# isStudent=True              # boolean 
# box=None                    # None
# list=[1,2,3]                # List
# tup=(12,25)                 # Tuple
# dic={                       # dictionary
#     'name':"Qasim",
#      'age':25
#      }

# print(name,type(name),floot,num,isStudent,box)
# for i in list:
#       print(i)
  
# for i in tup:
#       print(i) 

# for key in dic:
#       print(key)
 
# for value in dic:
#       print(value)  
      
# for key, value in dic.items():
#       print(key,":",value)  
      

# #ARITHMATIC OPERATORS

# a=30
# b=20
# sum1_=a+b
# minus=a-b
# multiply=a*b
# expo=a**b
# divid=a/b
# modulas=a%b
# print(sum1_)            
# print(minus)            
# print(multiply)            
# print(expo)            
# print(divid)            
# print(modulas)   


# #COMPARISION OPERATORES 

# print(a==b)           #false
# print(a!=b)           #true
# print(a>=b)           #true
# print(a<=b)           #false
# print(a<b)            #false
# print(a>b)            #true

   
# # ASSIGNMENT OPERATORS

# c=12
# print(c)
# c+=2
# print(c)

# c-=2
# print(c)

# c*=2
# print(c)

# c**=2
# print(c)

# c/=2
# print(c)

# c%=2
# print(c)


# # LOGICAL OPERATORS 

# age_=16
# if age_>=18 and age_<+50:
#   print("Young man") 
#   if age_<18:
#     print("Yonuger")
#   else:
#     print("Old Man") 


# passenger="ticket"
# if passenger=="ticket" or passenger=="card" :
#    print("Passenger is allowed to travel.") 
# else:
#     print("Not Allowed.")
       
    
# print(not True)
 
 
 
#   #TYPE CONVERSION
# #  1)- IMPLICIT TYPE CASTING        (auto conversion of data type) 
# num1=12        
# num2=12.2
# implicit=num1+num2
# print(implicit)
# print(type(implicit))


        
# #  2)- EXPLICIT TYPE CASTING        (manualy conversion of data type)

# strnum="12"
# explicit=int(strnum)
# print(explicit)
# print(type(explicit)) 


# strnum=""
# explicit=bool(strnum)
# print(explicit)
# print(type(explicit)) 


# # PROMPT FUNTION (INPUT)

# NAme=input("What is your name: ")
# Age=input("What is your age: ")

# print(f'Your name is {NAme} and age is {Age}')

# firstnum=int(input("Type first number: "))
# secondnum=int(input("Type second number: "))
# operators=input("Select operator +,-,*,/: ")

# if operators=="+":
#   print("After sum is ",firstnum + secondnum )
# elif operators=="-":
#   print("After minus is ",firstnum - secondnum )
# elif operators=="*":
#   print("After multiply is ",firstnum * secondnum )
# elif operators=="/":
#   print("After devide is ",firstnum / secondnum ) 
# else:
#   print("Choose one of the given operators.")  
  
  
  
# #  DEATAIL LEARNING OF STRING

# #CANCATINATION AND LENGTH

# firstname="Qasim"     
# lastname="Bhalli" 
# fullname=firstname+lastname
# print(fullname) 
# print(len(fullname)) 


# #INDEXING

# str1="Abul Qasim"
# # str1[1]="v"    #throw  error because string is immutable
# print(str1[1])

# #SILICING

# print(str1[1:7])      #start from index 1 and end on 6
# print(str1[:7])      #auto start from 0
# print(str1[1:7])      #start from index 1 and end on 6
# print(str1[-1:])      #start from reverse and reverse indexing start from -1


# # STRING FUNCTIONS

# print(str1.endswith("im"))
# print(str1.capitalize())
# print(str1.replace("Q","q"))
# print(str1.find("Qasim"))
# print(str1.count("i"))



# # USE OF IF ELIF ELSE AND INUT


# evenOdd=int(input("Type any number : "))

# if evenOdd%2==0:
#   print("Your number is even.")
# else:
#   print("Your number is odd2.")  
  
# isfactor=int(input("Type any number : ")) 
# if evenOdd % isfactor==0:
#   print("It is factor.") 
# else:
#   print("It is not factor.") 
 
 
 
#  # DETAIL LEARNIG OF LIST
 
# marks=[78,59,67,83,73]         # can store differet type of data

# marks[3]=78                    # assign new value because list is muteable(changable)
# print(type(marks))             #type is list  
# print(marks.remove(78))        # element that want to remove
# print(marks.pop(1))            # remove of index that you want 
# print(marks[0])  

# #ITERATION

# for i in marks:
#   print(i)
  
  
# #  INPUT FOR ADD IN LIST  

# tools=[]
# tool=input("Type required tools for BNR : ")
# tools.append(tool)
# tool=input("Type required tools for BNR : ")
# tools.append(tool)
# tool=input("Type required tools for BNR : ")
# tools.append(tool)
# tool=input("Type required tools for BNR : ")
# tools.append(tool)

# print(tools) 
  
# # LIST METHODS

# print(marks.append(78))             # add in list 
# print(marks.sort())                 #  sorting
# print(marks.reverse())              #  reverse 
# print(marks.insert(0,66))           #  index and element  (add at specified)
  
  
  
# # DETAIL LEARNING TUPLE

# tup1=()
# print(tup1) 
# print(type(tup1))           #tuple

# tup2=(1)
# print(tup2) 
# print(type(tup2))           # integer

# tup3=(1,)
# print(tup3) 
# print(type(tup3))           # tuple

# tup4=(1,2,3,4)
# # tup4[1]=5                   # throw error because tuple is immutable
# print(tup4[1])              #  has feature of indexing
# print(tup4.count(3))              #  has feature of count the occurance of element
# print(tup4) 
# print(type(tup4))           # tuple



# #DICTIONARY

# Dic1={
#   "name":"Abul Qasim",
#   "Age":25,
#   "Habits":{                   #nested dictionary
#     "Drinking":False,
#     "Smooking":False,
#     "Reading":True,
#   }
# }

# print(Dic1)                 #simple print of complete dictionary
# print(Dic1["Age"])          # print of one key
# print(Dic1["Habits"])        #print of nested divtioary
# print(Dic1["Habits"]["Drinking"])        #print of nested divtioary value
# Dic1["Age"]=30              #reassign the value
# print(Dic1)


# # METHODS OF DICTIONARY

# print(len(Dic1.keys()))
# # print(list(Dic1.keys()))            # change the data type
# print(Dic1.keys())
# print(Dic1.values())
# print(Dic1.items())
# print(Dic1.get("keys"))             # return N one if not found
# Dic1.update({
#   "Sex":"male"
# })
# print(Dic1.keys())


# # SET

# set1={1,2,3,4,4,5,True,"Qasim",(12,13)}                 # Not indexing, immuteable, unique element, not store muteable data type like list and dictionary
# set2={2,4,4,5,"Qasim",(12,13)} 

# print(set1)
# print(type(set1))

# coll1={}         # dictionary
# coll2=set()         # Set
# coll={1}         # set

# #NETHODS OF SETS

# set1.add(12)
# set1.remove(1)        # remove the element
# set1.clear()          # remove all element
# # set1.pop()            # remove random elemet    

# set1.union(set2)               # conbine all elements
# set1.intersection(set2)      # common elements

# values={9,9.0}        # treat same value ignore the data type 
# print(values)

# #DICTIONARY EXAMPLE WITH INPUT

# # subjects={}

# # x=int(input("type phy marks : "))
# # subjects.update({'"phy":, x'})

# # y=int(input("type che marks : "))
# # subjects.update({"che : ", y})

# # z=int(input("type math marks : "))
# # subjects.update({"math : ", z})

# # print(subjects)

# # # LOOPS   FOR AND WHILE


# count=1

# while count>=5:
#   print("Hello")
#   count+=1
  
  
  
  
#   TABLE WITH INPUT FUNCTION

# n=int(input("Make The Table Of : ")) 
# i=1
# while  i<=10:
#       print(n*i)
#       i+=1

 
 
 #  USE OF BREAK AND CONTINUE KEYWORDS IN LOOP
 
# c=1
# while c<=5:
#       if (c==3):
#             break
#       print(c)      # 1,2 
#       c+=1
      
# c=1
# while c<=5:
#       if (c==3):
#             c+=1
#             continue    # skip the number 3
#       print(c)
#       c+=1 
      
      
      
#         FOR LOOP

# mark=[12,24,23,54,23]
# for i in mark:
#   print(i) 
# else:
#   print("loop end")     # use in break otherwise throw error  
# mark=(12,24,23,54,23)     # same fo tuple
# for i in mark:
#   print(i)       


# alph=("abcdefghijklmnopqrstuvwxyz")
# word=input("Type any aphabit : ").lower() 

# ind=0
# for i in alph:
#   if (word==i):
#     print(f'{i} if found at index {ind}')
#     break
#   ind+=1


#      RANGE AND FOR LOOP

# range(start,stop,step)

# for i in range(5):
#   print(i)
# print("loop1 end")

  
# for i in range(1,5):
#   print(i)
# print("loop2 end")
  
  
# for i in range(1,5,2):
#   print(i)
# print("loop3 end")

# PASS KEYWORD IN LOOP


# for i in range(1,5,2):
#   pass      # function without work throw error but pass control it
# print("loop4 end")



# sum=0
# for i in range(1,6):
#   sum+=i
# print("sum = ",sum)

 
# i=1
# while i<=6:
#   sum+=1
#   i+=1
# print("sum = ",sum)



#      FUNCTIONS
#Simple function

#one method

# def sum(a,b):
#   print(a+b)  
# sum(3,5) 

#another method


# def sum(a,b):
#       return a+b 
# Sum=sum(3,5)
# print(Sum)  
      
      
      
      
      # RECURSION FUNCTION(ALTERNATE OF LOOP) 
      
# def  recurCount(n):
#   if (n==0):       # base of stoping condition
#     return
#   print(n)
#   recurCount(n-1)
# recurCount(4) 


# facoriol with recursion

# def fact(n):
#   if (n==0 or n==1):
#     return 1
#   else:
#     return fact(n-1)*n

# print(fact(5))

# list elements print with recursion 

# fruits=["apple","mangoe","banana","orange"]
# vaagetable=["ptato","ladybird","tamato"]  

# def itrate(list,index=0):
#        if(index==len(list)):
#          return
#        print(list[index])
#        itrate(list,index+1)
# itrate(fruits) 


#   FILE INPUT AND OUTPUT

# f=open("demo.txt","r")
# data=f.read(5)
# print(data)
# f.close()  

# f=open("demo.txt","r")
# data=f.readline()
# print(data)
# f.close()     

# f=open("sample.txt","a")
# f.write("I am Qasim.")
# f.close() 
# f=open("sample.txt","r+")
# f.write("You")
# f.close()
# f=open("my.txt","w")
# f.write("Hello Qasim")
# f.close() 

# with open("demo.txt","r") as f:
#       data=f.read()
#       print(data)
# import os

# os.remove("my.txt")  #to delete file


# with open("sample.txt","w") as f:    #auto close the file
#       data=f.write("Hello Qasim \nHow are you.")
#       print(data)
# with open("sample.txt","r") as f:    #auto close the file
#       data=f.read()
#       print(data)
# DataChange=data.replace("Qasim","Anas")
# print(DataChange)
# with open("sample.txt","w") as f:    #auto close the file
#       data=f.write(DataChange)    


word="Anas"
with open("sample.txt","r") as f:    #auto close the file
      data=f.read()
      if (data.find(word) != -1):
            print("Found")
      else:print("Not Found")
                  
  