def create():
    print("Creating")
    print("Creation successful")
    print("Is there anything else I can help with? C - create password, V - view passwords, Q - exit program")


def view():
    print("Viewing all credentials")
    print("Is there anything else I can help with? C - create password, V - view passwords, Q - exit program")


print("Welcome to Password Manager! What can I help you with? (C - create password, V - view passwords, Q - exit program)")
running = True
while(running):
    userResponse = input()
    if(userResponse.lower() == 'c'):
        create()
    elif(userResponse.lower() == 'v'):
        view()
    elif(userResponse.lower() == 'q'):
        running = False
        print("Program exiting...")
    else:
        print("Please enter a valid command. C - create password, V - view passwords, Q - exit program")

# f = open(r"C:\Users\Herman\Desktop\PManager\PMan.txt", "w")
