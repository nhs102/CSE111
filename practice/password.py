account = input("Enter your ID: ")
pw = input("Enter your PW: ")

if account == "nhs102" and pw == "990825":
    print("Login succeed")

else:
    print("Try it again")

i = 0
while account != "nhs102":
    i += 1
    