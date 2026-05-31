import re
import random
import string
import getpass

common_pass=["password123","password","admin","123456","qwerty"]

def password_checker(password):
    score=0
    suggestions=[]


    if len(password)>=8:
        score+=1
    else:
        suggestions.append("Use atleast 8 charcters.")

    if re.search(r"[A-Z]",password):
        score+=1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]",password):
        score+=1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d",password):
        score+=1
    else:
        suggestions.append("Add numbers.")


    if re.search(r"[!@#$%^&*()<>:|{}\"]",password):
        score+=1
    else:
        suggestions.append("Add any special character.")

    if password.lower() in common_pass:
        return f"very weak password" , ["This a very common password."]


    if score<=2:
        strength="WEAK!"
    elif score<=4:
        strength="MEDIUM!"
    else:
        strength="STRONG!"

    return strength,suggestions


def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("1. Check Password Strength")
print("2. Generate Password")

choice = input("Enter your choice: ")

if choice == "1":

    password = getpass.getpass("Enter your password: ")

    strength, suggestions = password_checker(password)

    print(f"\nPassword Strength: {strength}")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)

elif choice == "2":

    length = int(input("Enter password length: "))

    new_password = generate_password(length)

    print("\nGenerated Password:", new_password)

else:
    print("Invalid choice.")

