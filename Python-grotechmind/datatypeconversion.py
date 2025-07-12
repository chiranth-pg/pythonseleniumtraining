'''


1. Numbers
    i) Integer
    ii) Float
    iii) Complex

2. Sequential Data
    i) String
    ii) List
    iii) Tuple

3. Dictionary
4. Set
5. Bollean
'''

'''
##############Integer###########3
#int - float

num1=55
var1=float(num1)
print(var1, type(var1))

#int - string  #string follows indexing

num2=655565656
var2=str(num2)
print(var2, type(var2))

#int - list # conversion is not possible
num3=9899
var3=list(num3)
print(var3) #TypeError: 'int' object is not iterable


#int - tuple - conversion is not possible
#int - dic - not possible
#int - set - not possible

#int - Boolean

'''
num4=587
var4=bool(num4)
print(var4, type(var4))

num5=0
var5=bool(num5)
print(var5, type(var5))

#convert number digit into list value, 2 conversion is required
#int - string - list
a=234
var1=list(str(a))
print(var1)




##################float#####################

f1=55.89
f2=int(f1)
print(f2, type(f2))


#float - string

f2=3434.3434
v2=str(f2)
print(v2, type(v2), v2[-2])


#float - list - not possible
# float - tuple - not possible
# float - dict - not possible
# float - set - not possible
#
# float - boolean

f3=5.5
v3=bool(f3)
print(v3,type(v3))

f4=0.0
v4=bool(f4)
print(v4,type(v4))

####################String####################
#string - int -  possible - only when you have a number in the string


#string to float

str2="23.560"
v3=float(str2)
print(v3, type(v3)) #23.56 <class 'float'>

#string - list

str="python"
l1=list(str)
print(l1, type(l1), l1[2])

l1.append(40)
print(l1)

#string to tuple

str="Programming"
t1=tuple(str)
print(t1,type(t1), t1[-1])

#string - dict

timestamp - class 3rd february 43.50





