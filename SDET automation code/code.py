Day 1:
Data types:
# x="Arha"
# print(type(x)) # class string

x=100.0
print(type(x)) # class float

Simple Programming
#print("Hi my daughter name is Arha")
# a=100
# b=25
# print(a+b)

#-----
#comments in the python

'''this is python
this is python
this is python
this is python'''

"""this is python
this is python
this is python
this is python"""

#this is python

#short cut control + forward slash
# this is python
# this is python
# this is python
# this is python

#keywords in python
import keyword #print all the available keywords in python
print(keyword.kwlist)

Variables
#example 1
# a=10
# b=10.5
# c="arha"
# print(type(a))
# print(type(b))
# print(type(c))

#example 2
# a=10
# b=10.5
# print(a,b)

#example 3
# a,b,c=10,20,"Arha"
# print(a,b,c)

#example 4
# a=b=c=100
# print(a,b,c)

#example 5

x=1
y=2
print(x,y)
print(y,x)
x,y=y,x
print(x,y)

Day 2:
Arithematic Operations:
#arthematic operators
# a=5
# b=2
# print(a+b) #addition of a, b
# print(a-b) #subtraction
# print(a*b) #multiplication

# print(a/b) #2.5
# print(a//b) #2 quotient
# print(a%b) #1 remainder
# print(a**b) #5 power 2


#Relational operator / comparision operator
#Relatinal operators always returns True/False
# ><>= <= != ==
# a=5
# b=10
#
# print(a>b) #False
# print(a<b) #True
# print(a==b) #False
# print(a!=b) #True
# print(a<=b) #True
# print(a>=b) #False


# Logical operators
# and or not
#always returns boolean value True / False
a=True
b=False
print(a and b) #False
print(a or b) #True
print(not a) #False

#arthematic operators
# a=5
# b=2
# print(a+b) #addition of a, b
# print(a-b) #subtraction
# print(a*b) #multiplication

# print(a/b) #2.5
# print(a//b) #2 quotient
# print(a%b) #1 remainder
# print(a**b) #5 power 2


#Relational operator / comparision operator
#Relatinal operators always returns True/False
# ><>= <= != ==
# a=5
# b=10
#
# print(a>b) #False
# print(a<b) #True
# print(a==b) #False
# print(a!=b) #True
# print(a<=b) #True
# print(a>=b) #False


# Logical operators
# and or not
#always returns boolean value True / False
a=True
b=False
print(a and b) #False
print(a or b) #True
print(not a) #False

Concatination
#concatination

print(10+10) #20 Valid statment
print(10.5+12.0) #22.5 Valid statment
print(10+10.5) #20.5 Valid statment

print('welcome'+'python') #20 welcomepythonstatment

print(True+5) #not a valid statement becasue 2 values are different type
print(False+5) #not a valid statement becasue 2 values are different type
print(True+True) #not a valid statement becasue 2 values are different type

print(10+'welcome')
print(10.5+'welcome')
print(True+'welcome')


Conditional statement
#Conditional statement
#if, if..else, elif

#Example 1
# age=10
# if age>=18:
#     print("Eligle for the voting")
# else:
#     print("Not eligble for the voting")

#Example 2
# if True:
#     print("True condition")
# else:
#     print("false condition")

#Example 3
# if 1:
#     print("one")
# else:
#     print("Not one")

#Example 4
# num=11
# if num%2==0:
#     print("Given number is Even")
# else:
#     print("Given number is odd")

#Example 5

# if else in a single line (Ternary operation)
# num=10
# print("Even number") if num%2==0 else print("odd number")

#Example 5 - if else multiple statment in the single line
# a=20
# {print("hello"), print("python")} if a>=10 else {print("hi"), print("java")}

#Example 7 - multiple condition using elif statement

weeknumber=6

if weeknumber==0:
print("sunday")
elifweeknumber==1:
print("Monday")
elifweeknumber==2:
print("tuesday")
elifweeknumber==3:
print("wednesday")
elifweeknumber==4:
print("thursday")
elifweeknumber==5:
print("friday")
elifweeknumber==6:
print("saturday")
else:
print("Invalid week number")

Deleting variable
a=100
b=200
print(a)
print(b)

del a
print(a)
print(b)


Formatting output
#important!

#Approach 1
# name="Arha"
# age=6
# sal=50000
#
# print(name)
# print(age)
# print(sal)
#Approach 2
name,age,sal='Arha',6,50000
print(name,age,sal)
print(name,age)


#Approach 3
name,age,sal='Arha',6,50000
print("Name of the person is:", name)
print("Age of the person is:", age)
print("Salary of the person is:", sal)

#Approach 3
print("Name of the person is:%s Age of the person is:%d Salary of the person is:%g" %(name,age,sal))

#Approach 4
print("Name of the person is:{} Age of the person is:{} Salary of the person is:{}" .format(name,age,sal))
print("Age of the person is:{} Name of the person is:{}  Salary of the person is:{}" .format(age,name,sal))

Taking input from user
# Aprroach 1
# num1=input("Enter first number:")
# num2=input("Enter second number:")
#
# print(type(num1))
# print(type(num2))
#
# print(num1+num2) #since input we give in the run time would be considered as a String,so rather than addition it will concatinate in the output

# Aprroach 2

# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
#
# print(type(num1))
# print(type(num2))
# print(num1+num2)

# Aprroach 3 if the input is integer

# num1=input("Enter first number:")
# num2=input("Enter second number:")
#
# print(int(num1)+int(num2))

#aproach 4 if the input is decimal
num1=input("Enter first number:")
num2=input("Enter second number:")

print(float(num1)+float(num2))

Day 3:
For loop demo
#for loop
#print 1...10 numbers using for loop

# for i in range(10):
#     print(i)
#
# for i in range(1,11): # in operator help to pick the next number and store in the i variable
#     print(i)


#print only even numbers

# for i in range(0,21,2):
#     print(i)

#print only odd numbers
# for i in range(1,22,2):
#     print(i)

#print 10 to 1 in the decending order
# for i in range(10,0,-1):
#     print(i)

#

Jumping statement
#jumping statement - break and continue
# for i in range(1,10):
#     if i==5 :
#         break
#     print(i)
# print("program is ended here!")

# for i in range(1,10):
#     if i==3 or i==5:
#         continue
#     print(i)
# print("program is ended here!")


NumberDemo
num=10
num1=10.5
print(type(num)) #int
print(type(num1)) #float


print(max(10,20,200,30,30004,10)) #max function prints the maxmimum function - can be used for int and float
print(min(10,20,200,30,30004,10)) #min function prints the minimum function - can be used for int and float


Range function
#range - it will print values between the range

# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(list(range(1,10))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(list(range(1,10,3))) #[1, 4, 7]
#
# print(list(range(1,10,5))) #[1, 6]

#print only odd number

#print(list(range(1,10,2))) #[1, 3, 5, 7, 9]

#print(list(range(10,1,-2))) #[10, 8, 6, 4, 2]

print(list(range(-10,-1))) #[-10, -9, -8, -7, -6, -5, -4, -3, -2]

print(list(range(-10,-2,2))) #[-10, -8, -6, -4]

String Function
#example 1
# #create a string variable
#way of creating string variables
# s="string"
# s='string'
# s=str('string')
# s=str("string")
# #creating empty strings
# name=str() #name is a string variable but it doesnt have string variable
# name=""
# name=''

#example 2
#mutable and immutable
#mutable - can change the value of the vairable
#immutable - cannt change the value of the vairiable
#stirngs are immutable
#tuple is a immutable


# str="chiranth"
# print(id(str))
#
# str=str+'python'
# print(id(str))

# if the value is changed after the updation, then it is immutable


#example 3 - + and *
# str="Arha"
# print(str + "Pooja") # to concatinate the strings
# print(str*2) # to print the string value mulitple times

#Example4
#slicing the strings - by using slicing operators
#slicing operator []
#starting index - 0
#ending index - 1

# str="Arhabellur"
# print(str[1:4]) #rha
# print(str[:4]) #Arha
# print(str[2:]) #habellur
# print(str[1:-1]) #rhabellu

#Example 5
#ord() and chr()
# print(ord("A")) #to get the ASCII number of the character's
# print(chr(65))

#example 6
#max(), min() abndlen()

# print(max("abcd"))
# print(min("abcd"))
# print(len("abcd"))


#example7
# in and not in operators

s="welcome"
# print("come" in s) # true this operator returns - true/false
# print("lome" in s) # false

# print("come" not in s) # false
# print("lome" not in s) #true

#example 8 - string comparision
# print("tin"=="tie") #false
# print("free"!="freedom") #true
# print("Arrow" > "aron") #false
# print("arha">"aru") #false
# print("teeth"<="fellow") #false
# print("abc">"") #true

#Example 9 =Testing strings - True / False
# s="welcome to python"
# print(s.isalnum()) #false - string contains the numnber?
# print("Welcome".isalpha()) #True - is string contains contains only alphabets
# print("2012".isdigit()) #True
# print("first number".isidentifier()) #false - is it contain keyword - identifier - reserved keyword in pythin
# print(s.islower()) #true
# print("Welcome".isupper()) #false
# print(" ".isspace()) #True

#example seraching for substring

# s="welcome to python"
# print(s.endswith("thon")) #true
# print(s.startswith("good")) #false
# print(s.find("come")) #3 it finds the where come is location in the given string
# print(s.find("become")) #-1 it also finds it's not found in the string
# print(s.count("t")) #2 it counts number of occurences of substring the string

#Example 11 : Converting string
# s="String in PYTHON"
# s1=s.capitalize()
# print(s1) # String in python
#
# s2=s.title()
# print(s2) #String In Python-grotechmind
#
# s3=s.lower()
# print(s3) #string in python
#
# s4=s.upper()
# print(s4) #STRING IN PYTHON
#
# s5=s.swapcase()
# print(s5) #sTRING IN python
#
# s6=s.replace("in", "on")
# print(s6) #Strong on PYTHON


#Example 12: revere a string
#method1

# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("reveres string is:", rev_str) #emoclew

#method2
s="welcome"
rev_str=s[::-1] #s[starting point:ending point:-1]
print(rev_str)


Whileloop demo

#while loop
#print 1........10 number
# i=2 #intilization
# while i<=10:
#     print(i)
#     i=i+1
#     print("Done!")

#print 1 to 10 in decending order

i=10 #intilization
while i>=1:
print(i)
i=i-1
print("Done!")


Day 4:
List demo
#example1: how to create a list

# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple","10","banana",20]
# mylist=list() #emptylist
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

#example2: Accessing items from the list
# mylist=["apple","banana","cherry"] #in list index start from 0
# print(mylist[0]) #apple
# print(mylist[2]) #cherry
# print(mylist[-1]) #cherry

#example 3: Range of indexes
# mylist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[2:5]) #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1]) #['orange', 'kiwi', 'melon']

#example4: how to change the items value (item - value stored in the list)
# mylist=["apple", "banana", "cherry"]
# print(mylist) #['apple', 'banana', 'cherry']
# mylist[0]="orange"
# print(mylist) #['orange', 'banana', 'cherry']

#example5: Read items using loop statements
# mylist=["apple","banana",'cherry']
# for i in mylist:
#     print(i)

#example6: check if the item is exist in the list or not
# mylist=['apple','banana','cherry']
#
# if "orange" in mylist:
#     print("yes apple is present")
# else:
#     print('No orange is not present')

#example7: length (counting number of items in a list)
# mylist=['apple','banana','cherry']
# print(len(mylist)) #3

#example8: adding the items in the list append() - will add in the item at the end of the list
# insert() - will add the items at the desired place

# mylist=['apple','banana','cherry']
# print(mylist) #['apple', 'banana', 'cherry']
#
# mylist.append('orange')
# print(mylist) #['apple', 'banana', 'cherry', 'orange']
#
# mylist.insert(1,'kiwi') #['apple', 'kiwi', 'banana', 'cherry', 'orange']
# print(mylist)

#example 9 - Remove item from the list

#pop() - based on the index we can remove the item from the list

# mylist=['apple','banana','cherry']
# mylist.pop(0)
# # print(mylist)

# #del is not a fucntion, its a keyword

# mylist=['apple','banana','cherry']
# del mylist[2]
# print(mylist) #['apple', 'banana']

#clear() - clear is a function
# mylist=['apple','banana','cherry']
# mylist.clear()
# print(mylist) #[]

#example10: copy list
# mylist1=['apple','banana','cherry']
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)

#copy() method

# mylist1=['apple','banana','cherry']
# mylist2=mylist1.copy()
# print(mylist1) #['apple', 'banana', 'cherry']
# print(mylist2) #['apple', 'banana', 'cherry']

#example11: combine/join lists
#using + operator
# list1=['a','b','c']
# list2=['1','2','3']
# list3=list1+list2
# print(list3) #['a', 'b', 'c', '1', '2', '3']

#using loop statment - append function will add or new value to the list

# list1=['a','b','c']
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1) #['a', 'b', 'c', 1, 2, 3]

#using extend() function
list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]


Tuple demo
#example1: creating tuple

# mytuple=('apple','cherry','banana')
# print(mytuple)

mytumple=() #empty tuple

#example2 - access tuple items
# mytuple=('apple','cherry','banana')
# print(mytuple[1]) #cherry
# print(mytuple[-2]) #cherry

#Example3: Range of indexes
# mytumple=('aaple','banana','cherry','orange','kiwi','melon','mango')
# print(mytumple[2:5]) #('cherry', 'orange', 'kiwi')
# print(mytumple[-4:-1]) #('orange', 'kiwi', 'melon')

#example4: changing tuple items or values
#by default tuple does not allow you change values because it is immutable, but there is a workaround

#tuple --> list(modify) --> tuple
# mytuple=('apple','banana','cherry')
# mylist=list(mytuple)
# mylist[0]="orange"
# mytuple=tuple(mylist)
# print(mytuple) #('orange', 'banana', 'cherry')

#example5 : Reading tuple items using looping statement
# mytuple=('apple','banana','cherry')
# for i in mytuple:
#     print(i)

#Example6 : check if the item exists (searching of item in tuple)
# mytuple=('apple','banana','cherry')
# if 'banana' in mytuple:
#     print("yes banana is in mytuple")
# else:
#     print("No banana is not present")

#Example7: find the total numner of items in the tuple - Tupe length

# mytuple=('apple','banana','cherry')
# print(len(mytuple)) #3

#Example8: Add items into the Tuple - not possible because tuple is immutable - cannt change values / items

#Example9: copy tuple - yes we can copy since we are not changing anyvalues we can copy the tuples
mytumple1=('apple', 'banana','cherry')
mytumple2=mytumple1
print(mytumple2) #('apple', 'banana', 'cherry')

#Example10 : removing items from the tuple is not possible
# mytumple1=('apple', 'banana','cherry')
# mytumple1.remove('apple')
# print(mytumple1) #'tuple' object has no attribute 'remove'

#Example11 : Join / Combine the Tuple

tuple1=(10,20,30)
tuple2=('a','b','c')
tuple3=tuple1+tuple2
print(tuple3) #(10, 20, 30, 'a', 'b', 'c')

#Example12
tuple1=(10,20,20)
tuple2=('a','b','c')
if tuple1==tuple2:
print("tuples are equal")
else:
print("tuples are not equal")


Day 5
Dictionary demo
# #dictionarydemo - its unordered like set
# #example1
# mydic={101:'x', 102:'y', 103:'z'}
# print(mydic) #{101: 'x', 102: 'y', 103: 'z'}
#
# #example2: accessing items from dictionary
# mydic={
#     "brand":"maruthi",
#     "model":"Dzire",
#     "year":2020
# }
# print(mydic["brand"]) #maruthi
# print(mydic["model"]) #Dzire
#
#  #using get function
# mydic.get("year")
# print(mydic.get("year"))

#example3: change values in dictionary
# mydic={
#      "brand":"maruthi",
#      "model":"Dzire",
#      "year":2020
# }
# print(mydic) #{'brand': 'maruthi', 'model': 'Dzire', 'year': 2020}
# mydic["year"]=2023
# print(mydic) #{'brand': 'maruthi', 'model': 'Dzire', 'year': 2023}

#Example4: Reading items from dictionary using loop
# mydic={
#      "brand":"maruthi",
#      "model":"Dzire",
#      "year":2020
# }
# for i in mydic:
#     print(i) #prints only keys from dictionary
#
# for i in mydic:
#     print(mydic[i]) #prints only values from the dictonary
# for i in mydic.values():
#     print(i)  #prints only values from the dictonary

# for x,y in mydic.items():
#     print(x,y) # to print both the key and values in the dictonary

#Example5: Check key is exist in the dictionary or not
# mydic={
#      "brand":"maruthi",
#      "model":"Dzire",
#      "year":2020
# }
# if "model" in mydic:
#     print("yes model is present")
# else:
#     print("No model is not present")

#print("model" in mydic) #True

#Example6: find the length of my dictionary
# mydic={
#      "brand":"maruthi",
#      "model":"Dzire",
#      "year":2020
# }
# print(len(mydic)) #3

#Example7: Adding items to dictionary

# mydic={
#      "brand":"maruthi",
#      "model":"Dzire",
#      "year":2020
# }
# mydic["colour"]="red"
# print(mydic)

#Example8: Remove items from the dictionary
# mydic={
#      "brand":"maruthi",
#      "model":"Dzire",
#      "year":2020
# }
# mydic.pop("year")
# print(mydic)

#del mydic['year'] #can also be used this commond to delete the values
#mydic del #name error
# print(mydic)
# mydic.clear() #{}
# print(mydic)

#Example9 copying dictionay
mydic1={
"brand":"maruthi",
"model":"Dzire",
"year":2020
}
#without using copy function
# mydic2=mydic1
# print(mydic2)
#using copy function
mydic2=mydic1.copy
print(mydic2)
Setdemo
#example1 : creating set
# myset={'apple', 'banana','cherry'}
# print(myset) #output will not be ordered and same all the time

#example2 Accessing values or items from set
##only through loop we can access the set

# myset={'apple', 'banana','cherry'}
#
# for i in myset:
#     print(i)

#Example3 - calue exists in set or not

# myset={'apple', 'banana','cherry'}
# print("banana" in myset) #true
# print("banana11" in myset) #false


#example4: Adding items to set
#add() - add single item update() - add multiple items to set
# myset={'apple', 'banana','cherry'}
# # myset.add("orange")
# print(myset) #{'cherry', 'orange', 'apple', 'banana'}
#
# myset={'apple', 'banana','cherry'}
# myset.update(["kiwi,cheeku,kiwi11"])
# print(myset) #{'banana', 'kiwi,cheeku,kiwi11', 'apple', 'cherry'}


#example5: find mumber of items in a set
# myset={'apple', 'banana','cherry'}
# print(len(myset)) #3



#Example6: remove item from set - remove() , discard()
#by remove method
# myset={'apple', 'banana','cherry'}
# myset.remove("cherry")
# print(myset) #{'banana', 'apple'}



#discard method
# myset={'apple', 'banana','cherry'}
# myset.discard("apple") #discard function wont show any error while trying to remove the item which is not there in the set
# print(myset)


#example7 : clear all items from set
#myset={'apple', 'banana','cherry'}
# myset.clear()
# print(myset) #set()


#del myset
#print(myset)


#Example8: Joining 2 sets - union()
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3) #{1, 2, 'b', 3, 'a', 'c'}

#update()
set1={'a','b','c'}
set2={1,2,3}
set1.update(set2)
print(set1) #{1, 2, 3, 'a', 'c', 'b'}

Day6:
Functions
#Example1
# def myfun(): #here def is the keyword myfun is the function which should be mentioned with the brackert
#     print("Hi Arha")
# myfun()   # syntax for calling function

#Example2
# def myfun(name):
#     print("Hello", name)
# myfun("Arha")

#Example3
# def cal(a,b):
#     return (a+b) #if you are using the return stamment, the result has to be stored in the variable here sum is the variable
# sum=cal(198980,20)
# print(sum)
#print(cal(10,10))

#Example4:
# def func():
#     return
# print(func())
#
# def func():
#     i=10
# print(func())

#Example5:
# def cal(a,b):
#     print(a+b)
# cal(10,44)

#EExample6:
def cal(a,b):
return(a+b)
print(cal(10,44))

Global and Local variable

#Example1
# global_var=10 #global variable can be accessed inside the function also
#
# def func():
#     local_var=30
#     print(local_var)
#     print(global_var)
# func()
#
# print(local_var) #invalid statmentbcus local variable cannt be accessed outside the function

#Example2:
# xy=100
# def cool():
#     xy=200
#     print(xy)
# cool() #200


#Example3: changing the value of global vairble inside the function
# when the name is same as local and global vairbale

# xy=100 #global variable
# def cool():
#     global xy
#     xy=300
#     print(xy)
# cool() #200

#Example4:
# x=100
# def cool():
#     global x
#     x=500
#     print(x)
# cool() #if this call is not done, print(x) value will be 100 not 500
# print(x)

#Example5: Global variable can be created inside the fucntion but need to use the global keyword

# def cool():
#     global x
#     x=100
#     print(x)
# cool()
# print(x) #able to access the x, bcus x is global variable

#Example6:

Types of Arguments
#example1

# def func(i,j):
#     print(i,j)
#
# func(10,20) #Positional Argument
# func(j=10,i=20) #keyword Argument

#Example2: default values assigned to positional arguments

# def func(i,j=10):
#     print(i,j)
# func(100,200) #100 200
# func(1) #100 10

#Example3: keyword arguments
# def greetings(name,greetmsg):
#     print(greetmsg, name)
# greetings(name="arha", greetmsg="hello")
# greetings(name="hello", greetmsg="arha")

#example4:
# def my_func(a,b,c):
#     print(a,b,c)
# my_func(10,20,30) #Positional Argument
# my_func(a=20,b=20,c=20) #keyword Argument
# my_func(b=40,a=20,c=20) #keyword Argument
# my_func(40,20,c=20) #conbination of positional and keyword argument
# my_func(40,b=20,c=20) #conbination of positional and keyword argument
# my_func(c=40,10,20) #wrong statement because positional argument must appear before any keyword argument
# my_func(10,20,b=10) #logical error statment

#example5:function can return multiple value
def largest(a,b):
if a>b:
return a,b
else:
return b,a
print(largest(100,200))
print(largest(10,5))

Day 7:
OOPS concept
#Example1:
# class Myclass:
#     def myfun(self):  #creating class
#         pass
#     def display(self):  #self representing class, it should be there
#         print("john")
# mc1=Myclass() #creating object
# mc1.myfun()  #call method from the object
# mc1.display() #call method from the object

#Example2

# class Myclass:
#     def m1(self):
#         print("this is instance method..")
#     @staticmethod
#     def m2(self,num): #here self is also considered as a parameter and it doesnt belong to the class
#         print(self,num)
#
# mc=Myclass
# mc.m1(1)
# mc.m2(10,20)
# Myclass.m2(100,200) #calling static method directly using class not through object

#Example3
# class Myclass:
#     a,b=10,20
#     def add(self):
#         print(self.a+self.b) #self variable is used the access the class vairiables inside the method
#     def mul(self):
#         print(self.a+self.b)
# mc=Myclass()
# mc.add()
# mc.mul()

#Example4:
#global variable, class variable and local variable
#
# i,j=15,25 #global variable
# class Myclass():
#     a,b=10,20 #class vairable
#     def add(self,x,y):
#         print(x+y) #x,y are the local variable
#         print(self.a+self.b) #a,b are the class variable
#         print(i+j)
# mc=Myclass()
# mc.add(100,200)

#Example5:
#working with global, class and local variables
# a,b=15,25 #global variable
# class Myclass():
#     a,b=10,20 #class vairables
#     def add(self,a,b):
#         print(a+b) #local
#         print(self.a+self.b) #class vairables
#         print(globals()['a']+globals()['b']) #able to access global variables
#
# mc=Myclass()
# mc.add(100,200)

#Example6: one class can have multiple objects

# class Myclass():
#     def display(self,name):
#         print("This is display method")
#         print(name)
#
# obj1=Myclass()
# obj1.display("Arha")
#
# obj2=Myclass()
# obj2.display("Pooja")

#Example7:
#constructor examples

# class Myclass():
#     def __init__(self):
#         print("this is constructor..")
#     def m1(self):
#         print("Hello...")
# mc=Myclass() #invoke constructor automatically
# mc.m1()

#Example8:
# class Myclass:
#     name="Arha" #class variable
#     def __init__(self,name): #name is a constructor variable / local variable
#         print(name)
#         print(self.name)
# mc=Myclass("Arha")

#Example9:
#Req: Employee class
# class Emp:
#     def __init__(self,eid,ename,sal): #construtor
#         self.eid=eid     #converting local variables into class variables, all these belongs to class not to the constrcutor
#         self.ename=ename #converting local variables into class variables
#         self.sal=sal     #converting local variables into class variables
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# e1=Emp(101,"Arha",505050)
# e1.display()
# e2=Emp(101,"pooja",505050)
# e2.display()

#Example10:
#req: Emp
     #constrctor : eid,ename,sal
     #constrcutor : print eid,ename&sal
# class Emp:
#     def __init__(self,eid,ename,sal): #construtor
#         self.eid=eid     #converting local variables into class variables, all these belongs to class not to the constrcutor
#         self.ename=ename #converting local variables into class variables
#         self.sal=sal     #converting local variables into class variables
#     def __str__(self):
#         return(self.ename)
# e1=Emp(101,"Arha",505050)
# print(e1)

Day 8:
Inheritance
#example1:
# class A: #independent class
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A): #child of A
#     def m2(self):
#         print("this is m2 method from class B")
# bob=B() #here bob is variable and B() is a class
# bob.m1() #this is m1 method from class A
# bob.m2() #this is m2 method from class B

#Example2: Single Inheritance

# class A: #class contains variables and methods
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b) #class B contains total 4 variable and 2 methods
# bob=B() #can access both class A and class B
# bob.m1()
# bob.m2()

#Example3: Multiplevel inheritance
#combination of multiple single inheritance

# class A: #class contains variables and methods
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A): #B acqioredeverthing from A
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b) #class B contains total 4 variable and 2 methods
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cboj=C()
# cboj.m1() #30
# cboj.m2() #-100
# cboj.m3() #10



#Example4: Hierarachy inheritance - one parent can have multiple child

# class A: #class contains variables and methods
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A): #B acqioredeverthing from A
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b) #class B contains total 4 variable and 2 methods
#
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()
# bobj.m2()
# cobj=C()
# cobj.m1()
# cobj.m3()

#Example5: Multiple Inheritance - Two parents for one child

# class A: #class contains variables and methods
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B():
#     a,b=100,200
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


#Example6: calling parent class method using child class(Super class)
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")
#         super().m1() #it is used to invoke the parent class thorugh child
# bobj=B()
# bobj.m1() #This is m1 method from class B #this is m1 method from class A

#Example7:
# class A:
#     a,b=10,20
# class B(A):
#     i,j=100,200
#     def m(self, x,y):
#         print(x+y) #local variables
#         print(self.i+self.j) #class variables
#         print(self.a+self.b) #class variables
#
# bobj=B()
# bobj.m(1000,2000) #3000 300 30

#Example8: Overriding variables
# class Parent:
#     name="Arha"
# class Child(Parent):
#     name="Pooja" #overriding the variable value
# cobj=Child
# print(cobj.name) #Pooja

#Example9: Overriding methods
# class Bank:
#     def rateofintrest(self):
#         return 0
# class XBank(Bank):
#     def rateofintrest(self):
#         return 10
#
# class YBank(Bank):
#     def rateofintrest(self):
#         return 12
#
# objx=XBank()
# print(objx.rateofintrest()) #10
#
# objx=YBank()
# print(objx.rateofintrest()) #12

#Example10: Overloading concept (Polymorphism)

# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello" +name)
#         else:
#             print("Hello")
# h=Human()
# h.sayhello("Arha")
# h.sayhello()

#Example11 : Overloading 2 - One method different forms

class Calculation:
def add(self,a=0,b=0,c=0):
print(a+b+c)
calobj=Calculation()
calobj.add() #0
calobj.add(10,20) #30
calobj.add(10,20,30) #60


Day 10
Exception handling
#Example1

# print("this is the starting point of the programm")
# print("this is the starting point of the programm")
# print("this is the starting point of the programm")
# print("this is the starting point of the programm")
#
# try:
#     print(x)
# except:
#     print("Excetionoccured")
#
# print("This is the end point of the program")
# print("This is the end point of the program")
# print("This is the end point of the program")

#Example2
# print("This is the starting point of program")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Exception is handled")
# print("Program is completed")

#Example3 Multiple Except blocks - try except else finally
# try:
#     num1,num2=10,2
#     result=num1/num2
#     print("result is: ", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception")
# except SyntaxError:
#     print("Thrown syntax exception")
# except:
#     print("Exception handled")
# else:
#     print("No excpetion handled")
# finally:
#     print("Always excuete")

#Example4:
def enterage(num):
if num<0:
raise ValueError("Only Intergers are allowed")
if num%2==0:
print("Even")

else:
print("odd")
print("Checking number is even or odd by calling function")
num=2
try:
enterage(num)
except ValueError:
print("value error excpetionoccured and handled")
print("Programm completed")

Handling files

#Example1: writing data into text file

file=open("C:\demofiles\myfile.txt",'w')
file.write("this is my first statment\n")
file.write("this is my second statment\n")
file.write("this is my third statment\n")
file.write("this is my fourth statment\n")
file.close()
print("Program completed")

##Example 2 : Reading data from text file
file=open("C:\demofiles\myfile.txt",'r')
#print(file.read()) #this will read the entire content there in the file
print(file.readline()) #this will read the first line
file.close()

#Example 3: Appending data into text file

file=open("C:\demofiles\myfile.txt",'a')
file.write("\nthis is my sixth line\n")
file.write("this is my seventh line\n")
file.close()

