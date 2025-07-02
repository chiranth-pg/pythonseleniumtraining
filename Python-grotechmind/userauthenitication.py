
user_details = [
    ('user1', 'user@123'),
    ('user2', 'user2_123'),
    ('user3', 'user3@123'),
    ('user4', 'user4@123')
]

username= input("Please enter username: ")
password= input("Please enter password: ")

user_entry = (username, password)

if user_entry in user_details:
    print("Correct password")
else:
    print("Wrong credentials")