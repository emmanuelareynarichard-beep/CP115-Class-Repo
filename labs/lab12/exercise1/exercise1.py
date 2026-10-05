correct_password = "python123"
attempts_used = 0
login_successful = input("Enter your password:")
while attempts_used < 3:
        if login_successful==correct_password:
                break
        else:
                attempts_used +=1
                login_successful = input(f"Wrong password,you have {3 - attempts_used} attemps left:")

print(login_successful)
print(attempts_used)
