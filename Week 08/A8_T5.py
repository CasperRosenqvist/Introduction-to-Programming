

import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"




def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def load_users():
    users = []
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(DELIMITER)
            if len(parts) == 3:
                users.append({"id": int(parts[0]), "username": parts[1], "password": parts[2]})
    return users


def get_next_id(users):
    if not users:
        return 0
    return max(user["id"] for user in users) + 1


def save_user(username, password_hash):
    users = load_users()
    user_id = get_next_id(users)
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{user_id}{DELIMITER}{username}{DELIMITER}{password_hash}\n")
    print("User registration completed!")


def authenticate(username, password):
    users = load_users()
    password_hash = hash_password(password)
    for user in users:
        if user["username"] == username and user["password"] == password_hash:
            return user
    return None


def main_menu():
    print("Options:")
    print("1--Login")
    print("2--Register")
    print("0--Exit")


def user_menu():
    print("User menu:")
    print("1--View profile")
    print("2--Change password")
    print("0--Logout")


def register():
    username = input("Insert username: ")
    password = input("Insert password: ")
    password_hash = hash_password(password)
    save_user(username, password_hash)


def login():
    username = input("Insert username: ")
    password = input("Insert password: ")
    user = authenticate(username, password)
    if user:
        print("Authentication: successful!")
        while True:
            user_menu()
            choice = input("Your choice: ")
            if choice == "1":
                print(f"Profile ID: {user['id']} -- {user['username']}")
            elif choice == "2":
                print("Change password: (not implemented)")
            elif choice == "0":
                print("Logging out...")
                break
    else:
        print("Authentication: failed!")


def main():
    print("Program starting.")
    while True:
        main_menu()
        choice = input("Your choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "0":
            print("Exiting program.")
            break
    print("Program ending.")


main()
