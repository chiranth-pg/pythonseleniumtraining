#split method - this method break the string from given delimenters and return as list

str="Today is very sunny day"

output = str.split(" ")
print(output)

for word in output:
    print(word, ":", word[::-1])


str1="Python, Programming, Language"
print(str1.split(","))
print(str1.split("p"))
print(str1.split("g"))


url="https://www.gogle.co.in"

print("_"*50)
protocol=url.split(":")[0]
print("protocol: ", protocol)

print("_"*50)
server=url.split(".")[1]
print("server: ", server)

print("_"*50)
www=url.split(".")[0].split("//")[1]
print("www: ", www)

print("_"*50)
xx=url.split("//")
print("xx: ", xx)


#Replace method: replace any substring or character from target string
print("_"*50)
strb="Hello good morning, hope you are doing good"
result=strb.replace("good", "bad") #we can add multiple .replace
print("result", result)


strb="Hello good morning, hope you are doing good"

word_list=strb.split(" ")
output= ""
count=0
for word in word_list:
    if "good" in word and count==0:
        output = output+ "bad" + ""
        count+=1
    elif "good" in word and count==1:
        output=output+"nice" + " "
    else:
        output=output + word+ " "
print("Output : ", output)


#count method = This method return count of any character / sub-string repeated in given target string.

str="Hello good morning, hope you are doing good"
print("Count of good:", str.count("good"))

#index method : This method provide index position of any character or substring

print("_"*50)
str="Hello good morning, hope you are doing good"
print("index of o: " , str.index("o"))


#find method : This method return the index position of the character or substring
str="Hello good morning, hope you are doing good"
print("Check substring line : ", str.find("good"))

#strip() method : this method used to remove the trialing space, means space in begining and end of the string

strk="    hi arha    "
print(strk)
print(strk.strip())
print(strk.replace(" ", "")) #removes the space
#removes space
#lstrip - remove space from left side
#rstrip - remove space after right side


#remove all spaces
print(strk.replace(" ", "")) #removes the space