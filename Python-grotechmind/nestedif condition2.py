# age = 17
# if age >= 18:
#     print("Adult")
#     if age >= 21:
#         print("You can drink alcohol in the US")
#     else:
#         print("You can't drink alcohol in the US")
# else:
#     print("Minor")


print("_" * 100)
round1="Pass"
round2="Pass"
round3="Pass"

if round1 =="Pass":
    print("Congrats first round is clear")
    if round2=="Pass":
        print("Congrats second round is also clear")
        if round3=="Pass":
            print("Congrats you are pass")
        else:
            print("Failed in 3rd round better luck next time")
    else:
        print("sorry , you are failed in second round")

else:
    print("sorry you are failed")