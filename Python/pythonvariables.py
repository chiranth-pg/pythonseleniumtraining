var1=10
var2=20
var3=10
print(id(var1)) #140733690692808
print(id(var2)) #140733690693128
print(id(var1)) #140733690692808

#Rules to define variables name
#variable name should not start with number
#there should not be any space in variable name
#python is case sensitive language variable name with upper case and lower case will be different


#asssign multiple values to multiple variables
p,q,r = 600,700,800
print("vale of p :", p)
print("vale of q :", q)
print("vale of r :", r)

#mathematical operations
"""
+ = plus operator
- = minus operator
* = multiplication
/ = division 
// = division wiht diuble slash
** = power operator 
"""

#addition of 2 numbers
var1=6
var2=25
var3 = var1+var2
print("Addition of 2 number: ", var3)

#multiplication
mul= var1*var2
print("Multiplication of 2 numbers:", mul)

#subtraction
sub=var2-var1
print("Subtraction: ", sub)

#division with single and double slash
div=var2/var1 #this will give point digit
div1=var2//var1 #this wont give the digit output
print("Division of 2 numbers: ", div)
print("Division of 2 numbers: ", div1)

#power operator
pow=var1**var2
print("power of var1: ",pow)

str=" Arha "
print(str*3)
print("_"*10)

#mathematical equation
#(a+b)2 = a2+b2+2ab

a=204
b=20
#LHS
lhs=(a+b)**2
print("LHS:",lhs)

#RHS
rhs=a**2+b**2+2*a*b
print("RHS:",rhs)