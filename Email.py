import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}"
user_eamil = input("Enter your Email:")

if re.search(email_condition,user_eamil):
    print("Right Email")
else:
    print("wrong Email")    