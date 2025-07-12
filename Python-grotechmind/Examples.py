str1="Hello Good Morning"
vowels="aeiou"
result=""

for char in str1:
    print(char)

    if char in vowels:
        continue
    else:
        result=result+char

print("result  :", result)
