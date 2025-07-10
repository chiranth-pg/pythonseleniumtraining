'''

Properties of string
It is immutable and it is defined we can not change it
Follows the positive and negative indexing for the data
Any value enclosed with single/double/triple quotes then it is consider as string

'''

# 1. string concatination
#Hello my name is Rahul and my age is 25 and living in Mumbai
name="chiranth"
age =36
city="Pune"

output = "Hello my name is " + name +" and my age is " + str(age) + " and living in " + city
print(output)


#2. Format method:
output1= "Hello my name is {} and my age is {} and living in {}".format(name,age,city)
print(output1)

#3 f string formatting
output2= f"Hello my name is {name} and my age is {age} and living in {city}"
print(output2)


name="Arhachiranth"
print(name[1])


#apply loop on string values
str="Python language"

for val in str:
    print(val, end="")

#loop with indexing
str_len = len(str)
for i in range(str_len):
    print(i, str[i])


######## String Slicing ################3
#Rule : str[intial index : last index]
#in this rule the output will always include the intial and excule the last index

