#!/usr/bin/env python3.6
from user import User
import getpass
import os
os.system('setterm -background white -foreground black -store')
def create_user(user_name,user_password,user_full_name,phone_number,email):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,user_password,user_full_name,phone_number,email)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)


def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

# MAIN FUNCTION
def main():

    print("Welcome to your Password Locker App.")

while True:
    print("*"*100)
    print("For old user => ou - For new User => nu - Display users => du \
    - To Find a User => fu - Create Credentials => cc - To Quit => qu")
    print("*"*100)
    short_code = input().lower()
    if short_code == 'eu':
        user_name = input("Enter User Name")
        user_password = input("Enter USer Password")

        # Open user file as read only

    elif short_code == 'nu':
        user_name = input("Enter user Name :")
        user_password = getpass.getpass('Enter your password :')
        user_full_name=input("Enter Full Name :")
        phone_number = input("Enter Phone Number :")
        email = input("Enter Email :")

        print("Thank you you info :" + user_name + ";" + user_password + ";" + user_full_name + ";"
        +phone_number + ";" + email)

        save_users(create_user(user_name,user_password,user_full_name,phone_number,email))
        print('\n')
        print(f"New User {user_name} {user_full_name} Created")

        new_user_info = (user_name + ";" + user_password + ";" + user_full_name + ";"
        +phone_number + ";" + email)

        print(new_user_info)
        new_user_info1=new_user_info.split(";")
        print(new_user_info1)
        print(new_user_info1[0])
        

        #Open User File as write and save new authantication
        users_info_file = open("user_info.txt","a+")
        users_info_file.write("\n"+new_user_info)
    elif short_code == "du":
        if display_users():
            print("Here is a list of all your contacts")
            print('\n')
            for user in display_users():
                print(f"{user.user_name} {user.user_full_name} .....{user.phone_number}")
                print('\n')
        else:
            print('\n')
            print("Sorry no users")

    elif short_code == "qu":
        print("Thanks")

        break
    else:
        print("Bad option, bye")
 

if __name__ == '__main__':

    main()
