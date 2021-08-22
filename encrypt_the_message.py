# encrypt the message

def input_message():
    while True:
        msg = input("Enter your message: ")
        if 0 < len(msg) < 1000:
            return msg
            break
        else:
            print("Length of the message shall not greater than 1000")
            print()

def input_key(msg):
    while True:
        try:
            key = int(input(f"Enter a number to encrypt or decrypt (not greater than {len(msg)}): "))
            if 0 < key <= len(msg):
                return key
                break
            else:
                print(f"The number you entered shall not greater than {len(msg)}. Try again")
                print()
        except ValueError:
            print("You shall input a positive integer, not decimal or string")
            print()

def choice():
    while True:
        try:
            option = int(input("""SELECT OPTION TO EXECUTE PROGRAM \n
    [1]. ENCRYPTION \n
    [2]. DECRYPTION \n
    Your choice (enter number only): \t"""))
            if option == 1 or option == 2:
                return option
                break
            else:
                print("You only have two options. Try again!!!")
                print()
        except ValueError:
            print("Try again!!!")
            print()

def reverse(string):
    string = string[::-1]
    return string

def encrypt(msg, key):
    Sb = reverse(msg[:key])
    Se = reverse(msg[key:])
    return (Sb + Se)

def try_again():
    choice = input("Do you want to continue (Y/N): ").lstrip().rstrip().upper()
    if choice == "Y" or choice == "YES":
        return True
    else:
        print("BYE! See you next time!!!")
        exit()

if __name__ == '__main__':
    while True:
        option = choice()
        msg = input_message()
        key = input_key(msg)
        if option == 1:
            print(f"The encrypted message is: {encrypt(msg, key)}")
        else:
            print(f"The decrypted message is: {encrypt(msg, key)}")
        print()
        try_again()
        print()