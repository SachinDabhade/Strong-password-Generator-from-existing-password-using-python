# ********************************* Making strong password from existing password and checking the strength of password ******************************

# Importing Libraries
import re

# This video is about securing and making the strong password using the exiting password with the help of your python programme
def strongPass(password):
    for a, b in StrongList:
        if a in password:
            password = password.replace(a, b)
    return password

# Module of regular expression is used with search()
def Check_1(Password):
    # Function one to check the password strength get by user
    if len(Password) >= 8:
        print('\n*****************************************************')
        print('Password Contain..')
        print(re.findall(r"[a-z]", Password))
        print(re.findall(r"[A-Z]", Password))
        print(re.findall(r"[_@$]", Password))
        print(re.findall(r"[0-9]", Password))
        print('*****************************************************')
        Pass = strongPass(Password)
        print('\nGenerating New Password...')
        print('\nRecommended Password: ',Pass)

    else:
        print("\nLength of password is so small...")
        exit()


if __name__ == '__main__':
    
    StrongList = (
    ('a', '@'), ('and', '&'), ('s', '$'), ('h', '#'), ('i', '!'), ('o', '0'), ('t', '|-'), ('b', '|>'), (' ', '_'),
    ('c', '<'), ('d', '|>'), ('l', '|'), ('9', '?'))

    # User input the password
    password = input("\nEnter Your Password: ")
    password = password.lower() # converting the password to the lower case
    # Checking the strength of password
    Check_1(password)
        
