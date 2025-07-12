#join method: can combine 2 given words

str2="python"
result = "-".join(str2)
print("result : ", result)


#check given has only numbers

str2="99898898"
print(str2.isnumeric()) #True

str2="9989  8898"
print(str2.isnumeric()) #False


str5="hello123"
print(str5.isalnum()) #True



print("_"*100)

word="""
The find method in 89898 Python is used to search for a substring within a string. It returns
The index of the first 9742477716 occurrence of the substring
If the substring is not found it returns 
If the substring is not 46974 2454  65 7 5
 97 5454 54 5454 54 54 found it returns chiranth@gmail.com
"""

word_list= word.split(" ")
print(word_list)
print("_"*100)
for word in word_list:
    if word.isnumeric() and len(word)==10:
        print(word)
    elif "@" in word:
        print(word)
    else:
        continue


print("_"*100)

#program: write a python programm to find out the longest word in the given string

str_input="user potpeorties and become a part of userkjdksjkjskfj s and ajeijeijwewjei"

longest_word= ''
long_len=0

wordddd= str_input.split()
for word in wordddd:
    word_len = len(word)
    print(word, word_len)
    if word_len > long_len:
        long_len = word_len
        longest_word = word
print(long_len, longest_word, ":", word)


print("_"*100)


#write program to get count of vowels from each word

str1="USer properies become part test"

word_list=str1.split(" ")
vowels= "aeiou"
output={}
count = 0
for word in word_list:
    for char in vowels:
        if (char in word) or (char.upper() in word):
            count+=1
        else:
            continue
    output[word] = count

print("Output : ", output)