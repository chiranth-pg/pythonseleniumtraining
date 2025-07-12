# Nested loop conditions
# While loop

# Nested loop conditions

# for i in range(1,5):
#     print("_" * 30)
#     print("Address :", i )
#     for j in range(1,4):
#         print("Package: ", j)
#
# print("_"*30)

#write a python programm to print start pattern

# for i in range(1,6):
#     for j in range(i):
#         print('arha', end=" ") #end here help to print in one single line
#     print() #tihs print will help to move to next line


# print(ord("A"))
# print(chr(66))
#
#
#
# temp=65
# for i in range(1,6):
#     for j in range(i):
#         print(chr(temp), end=" ")
#         temp = temp+1
#     print()




# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#
#     print()



########################### WHILE Loop Condition ###########################################33
#while loop to exceute the code

#print 1 to 9
temp =1
while temp<10:
    print(temp)
    temp+=1

#write infinite for loop
n=1
while True:
    print(n)
    n +=1


#find out the reverse of the any given number without using type casting

num = 12345
rev = 0

while num > 0:
    digit = num % 10         # Get the last digit
    rev = rev * 10 + digit   # Add it to the reversed number
    num = num // 10          # Remove the last digit from original number

print("Reversed number:", rev)

