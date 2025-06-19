#Integer data type


print("_"*50)
var1=2
var2=456
var3=9898656598
print(type(var1))
print(type(var2))
print(type(var3))

"""
Properties of Integer

-> Integer is immutable data type
-> Any whole number will be consider as integer
-> There is no specific range of limit for integer value, we can dfine any long numner is integer
"""


print("___________________float____________________")

var_1 =2.5

"""
Properties of float
Flot is immutable data type
any decimal number will be considered as float
there is no specific range or limit for float value, we can define any long number decimal number as float
"""



print("___________________enf of float____________________")
#complex number (x+yj)
#real number : x
#imaginary number : y



#Sequential data type

#String
'''
string is immutable data type
string follows the positive and negative indexing
we can store any long raw data as string

'''

'''
properties of list
list is mutable data type, we can modify the list at any point of time
list follows the similar positive and negative indexing as like string
all type of data ca store in the list, like, int, flot, string boolean, dict, list, tuple set
if we compare list and tuple, the nlist is a bit slower than tuple
'''

'''
tuple is immutable data type, we cannt modify once it is defined
tuple follows the positive nad negative indexing 
all type of data can be part of the tuple - int,float,string,list,tuple.dict,set,boolean
tuple is faster then list to access the data
tuple=(3,4,5,[3,5,6], (1,2,3), True, 'Arha')
'''

'''
#_______Dictionary______
dict1={'name': 'Arha', 'age': 7}
        key      value
dict is mutable data type, we can modify it any point of time
all keys should be unique in the dict, duplicate keys are not allowed
only imutable data type can key in the dic like int, float, string, tuple, boolean
we can set all type of data as dict vaue int, float, string, list, tuple, set, boolean
dict doesnt follow any indexing, it stores the data in unstructural
'''
dict1={'name': 'Arha', 'age': 7}
print(dict1, type(dict1))
dict1['email']='arhabc@gmail.com'
print(dict1)

#ways of defining dictionay
dict2={}
dict3[3]=[5,6,7]
dict4['hello']={'name',:'arha','age':25}
dict5[(2,4,5)]="python programing"


'''
properties of set

-- set is mutable data type, we can modify the data at any point of time
-- set only store unique data, duplicate data is not allowed
-- all the immutable data type can member of set, int, string, float, tuple, boolean
-- any mutable data type can not be a member of set eg list, dict and set
-- set store the data in random, it does not follow any indexing




'''


