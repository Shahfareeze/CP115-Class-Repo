correct_password = "python123"

# TODO: Your code here

attempts_used = 1
login_successful = False

password = input()
while attempts_used < 3:
    
    attempts_used += 1
    password = input()

    if password == correct_password:
        login_successful = True
        break

    


print(login_successful)
print(attempts_used)
