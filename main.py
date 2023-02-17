import random
import string

while True:
    len_password = int(input("How long would you like your password to be?: "))
    numberinput = input("Do you want me to include numbers?: (y/n) ")
    specialinput = input("Do you want me to include special characters?: (y/n) ")
    #This code here is only to practice dictionaries---------------
    isnumber = {"y": True, "n": False}
    isspecial = {"y": True, "n": False}
    #--------------------------------------------------------------
    password = []
    characters = list(string.ascii_letters)
    if isnumber[numberinput]:
        characters = characters + list(string.digits)
    if isspecial[specialinput]:
        characters = characters + list("!'#$%+()/,")

    random.shuffle(characters)

    for i in range(0,len_password):
        password.append(random.choice(characters))

    print("".join(password))
    exit_input = input("Type 'exit' to quit or press enter to generate a new password: ")
    if exit_input == "exit":
        print("Terminated.")
        break

