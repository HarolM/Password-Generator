"""This program is to demonstrate my ability with the use of multiple functions, encoding messages, working with SHA-256 algorithm, and retrieving
encoded messages to decrypt"""

"""MyPassword is a program that will generate a password for its user given certain instructions such as length, and the inclusion of
numbers or punctuations. This program will generate a password that the user can then save to an external file if they wish to. The program will
then convert the generated password to its hash value and store it, asking the user for more details surrounding what this password belongs to.
Additionally, if the user knows their password, they can verify to see if that password is actually being used, and by which program it is being
used by. If the user forgets the password, they will have been given a code that is saved in a separate file that is also encoded. With this code
they can retrieve the password as long as it has been previously saved."""


import random, string, hashlib, sys, csv

def main():
    while True:
        user_response = input(
            "Welcome to MyPassword, would you like to CREATE, VERIFY, or RETRIEVE a password? "
        ).lower()

        # If our user chooses to create, the program will prompt for length, use of symbols, and use of numbers. Once entered, program will generate a random password
        if user_response == "create":
            char_len = character_len("")
            use_symbols = yes_no_prompt("Does it require any symbols? ")
            use_numbers = yes_no_prompt("Does it require any numbers? ")
            password = generate_password(char_len, use_symbols, use_numbers)
            print(f"Your password is: {password}")
            save = yes_no_prompt("Would you like to save this password? ")

            # The user will have the chance to save the password, which will run the SAVE_PASSWORD function and write to a csv file
            if save:
                user = input("What does this password belong to? ")
                result = save_password(user, password)
                result2 = save_code(password)
                print(result)
                sys.exit(0)
            else:
                sys.exit(0)

        # Verifies user input. if password has been saved to the CSV found in the SAVE_PASSWORD function, it will be verified.
        elif user_response == "verify":
            current_pass = input("Enter current password: ")
            result = verify_password(current_pass)
            print(result)
            break

        # Uses the RETRIEVE function to decode a given code and return the users password
        elif user_response == "retrieve":
            user_input = input("Please enter your code: ")
            print(retrieve(user_input))

        # exits the program
        elif user_response == "exit":
            sys.exit("Thanks!")

        else:
            print("Please type CREATE, VERIFY, RETRIEVE or EXIT to exit the program")


# Length function, determines the length of the password between 8 to 64 characters
def character_len(leng):
    while True:
        leng = input("How many characters would you like your password to be? ")
        if leng.isdigit() and 8 <= int(leng) < 64:
            return int(leng)
        else:
            print("Response must be a digit between 8 and 64 characters")
            pass


# Function used multiple times throughout code. Will loop if incorrect input is entered
def yes_no_prompt(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["y", "yes", "yeah"]:
            return True
        elif response in ["n", "no", "nah", "nope"]:
            return False


# use of string library to generate a password given the user input of including numbers/symbols
def generate_password(char_len, use_symbols, use_numbers):
    while True:
        alpha = string.ascii_letters
        if use_symbols:
            alpha += string.punctuation
        if use_numbers:
            alpha += string.digits
        password = "".join(random.choice(alpha) for _ in range(char_len))

        if use_symbols and not any (char in string.punctuation for char in password):
            continue
        if use_numbers and not any (char in string.digits for char in password):
            continue

        return password


# Writes to password.csv file. Will throw error if this file does not exist.
def save_password(user, password):
    try:
        with open("password.csv", "a+") as file:
            writer = csv.writer(file)
            writer.writerow([user, hashlib.sha256(password.encode()).hexdigest()])
        return "Password saved successfully"
    except FileNotFoundError:
        return "Error: Password.csv Not Found in directory. Program will now exit"


# Writes to password_code.txt file, will throw error if txt file not found
def save_code(code):
    try:
        with open("password_code.csv", "a+") as file:
            plain_text = code
            shift = 7
            alpha = string.printable
            shifted = alpha[shift:] + alpha[:shift]
            table = str.maketrans(alpha, shifted)
            encryption = plain_text.translate(table)
            writer = csv.writer(file)
            writer.writerow([encryption])
        return "Password saved successfully"
    except FileNotFoundError:
        "Error: Password_code.txt Not Found in directory. Program will now exit"


# Decodes given code and converts that decryption into its hash value to compare if the password exists. If so, it will print out decrypted code
def retrieve(password):
    # first decrypt the code
    plain_text = password
    shift = 7
    password = string.printable
    shifted = password[-shift:] + password[:-shift]
    table = str.maketrans(password, shifted)
    decryption = plain_text.translate(table)
    hashed_password = hashlib.sha256(
        decryption.encode()
    ).hexdigest()  # hash that decryption

    # If hash value exists from that decrypted code, then return password.
    try:
        with open("password.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if hashed_password == row[1]:
                    return f"Your password is {decryption}"
            return "Password not found"
    except FileNotFoundError:
        return "Error: Password.txt not found in directory. Unable to verify password"


#  Compares hash values of user input and saved passwords
def verify_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open("password.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if hashed_password == row[1]:
                    return f"This password is in use by {row[0]}"
            return "This password is not in use"
    except FileNotFoundError:
        return (
            "Error: Password.csv not found in the directory. Unable to verify password"
        )


if __name__ == "__main__":
    main()
