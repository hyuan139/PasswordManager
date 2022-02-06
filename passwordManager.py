import secrets
import string


def add():
    add_helper()
    print("Add successful")
    print("Is there anything else I can help with? A - add existing credentials, C - create password, V - view credentials, Q - exit program")


def add_helper():
    pwdCorrect = False
    accountDomain = input("What is the domain for the account? ")
    username = input("What is the username? ")
    password = input("What is the password? ")
    while(not pwdCorrect):
        pwdCheck = input("Is " + password + " correct? Enter [Y]es or [N]o. ")
        if(pwdCheck.lower() == "y"):
            break
        else:
            password = input("Please re-type the password. ")
    # write credentials to the file
    add_credentials(accountDomain, username, password)


def create():
    create_helper()
    print("Creation successful")
    print("Is there anything else I can help with? A - add existing credentials, C - create password, V - view credentials, Q - exit program")


def create_helper():
    passwordLength = int(input(
        "What is the length of the password you desire? (Anything below 6 is defaulted to length 12). "))
    if(passwordLength < 6):
        passwordLength = 12
    inlcudeNumbers = input("Include digits in the password? [Y]es or [N]o. ")
    includeSpecialSymbols = input("Include special symbols? [Y]es or [N]o. ")
    passwordChoices = string.ascii_letters
    if(inlcudeNumbers.lower() == "y"):
        passwordChoices += string.digits
    if(includeSpecialSymbols.lower() == 'y'):
        passwordChoices += string.punctuation
    securePassword = "".join(secrets.choice(passwordChoices)
                             for i in range(passwordLength))
    print("Your generated password is " + securePassword)
    accountDomain = input("What is the domain for the account? ")
    username = input("What is the username? ")
    add_credentials(accountDomain, username, securePassword)


def view():
    print("Viewing all credentials...")
    f = open(r"C:\Users\Herman\Desktop\PManager\PMan.txt", "r")
    print(f.read())
    f.close()
    print("Is there anything else I can help with? A - add existing credentials, C - create password, V - view credentials, Q - exit program")


def add_credentials(aDomain, uName, pwd):
    credentialSeparator = "============================================="
    # Replace C:\Users\Herman\Desktop\PManager\PMan.txt with your PATH
    # e.g C:\Users\YOUR_NAME\Desktop\FILENAME.txt
    f = open(r"C:\Users\Herman\Desktop\PManager\PMan.txt", "a")
    f.write("Website: "+aDomain+"\n"+"Username: "+uName+"\n" +
            "Password: "+pwd+"\n"+credentialSeparator+"\n")
    f.close()
    print("Credentials added to file")


print("Welcome to Password Manager! What can I help you with? (A - add existing credentials, C - create password, V - view credentials, Q - exit program)")
running = True
while(running):
    userResponse = input()
    if(userResponse.lower() == 'a'):
        add()
    if(userResponse.lower() == 'c'):
        create()
    elif(userResponse.lower() == 'v'):
        view()
    elif(userResponse.lower() == 'q'):
        running = False
        print("Program exiting...")
    elif(userResponse[0].lower() not in ["a", "c", "v", "q"]):
        print("Please enter a valid command. A - add existing credentials, C - create password, V - view credentials, Q - exit program")
