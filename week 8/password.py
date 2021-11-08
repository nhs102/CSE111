cnt = 4

while True:

        # ID, PW 입력받기
        id = input("Enter your account: ")
        pw = input("Enter youe password: ")

        # ID and PW correct?
        if id == "nhs102" and pw =="990825":
            print("Login Succeed")
            break
        else:
            cnt -= 1
            print("Login Failed. (Remain attempt {})".format(cnt))

        if cnt <= 0:
            print("Limit login for security.")