#!/usr/bin/env python3.6
from user import User
from user import Credentials
import getpass
import os
import shutil
import string
import random
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


"""
Credentials
"""

def create_account(user_account_name,user_account_user,user_account_password):
    '''
    Function to create a new account
    '''
    new_account= Credentials(user_account_name,user_account_user,user_account_password)
    return new_account

def save_accounts(account):
        '''
        Function to save account credential
        '''
        account.save_account()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def find_account(name):
    '''
    Function that finds a user by name and returns the account
    '''
    return Credentials.find_by_number(name)

"""
MAIN FUNCTION
""" 
def main():
        print("Thanks for Using Password Locker App.")

while True:

    columns = shutil.get_terminal_size().columns
    print("PASSWORD LOCKER APPLICATION".center(columns))
    print("-"*220)

    print("Login =>(l)Register=>(r) Store Credentials => (st) Generate Random Password =>(ag) Generate Custome Psssword=>(cg) DIsplay Credentials=>(dc) Delete Credential=>(rc) Quit=>(q)")    
    options=input()

    if options=="r":
        print("Welcome")
        user_name = input("Enter user Name :")
        user_password = getpass.getpass('Enter your password :')
        user_full_name=input("Enter Full Name :")
        phone_number = input("Enter Phone Number :")
        email = input("Enter Email :")

        curUserName=user_name

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
        
        """
        Open User File as write and append new authantication
        """

        users_info_file = open("user_info.txt","a+")
        users_info_file.write("\n"+new_user_info)
        users_info_file.close()

    elif options == 'l':
        """
        Open User File as read only and append new authantication
        """
        user_get_info_file = open("user_info.txt","r")
        # print("Store Old Credentials => st - Automatic Password Generator => ag - Custom Password Generator => cg Display accounts => dc Delete Credentials => rm Exit App q")
    elif options == 'st':
        print("stroring New Credentials")

        user_account_name = input("Enter your application(ex.WhatsApp) :")
        user_account_user=input("Enter User Name :")
        user_account_password = getpass.getpass('Enter User password :')

        # print("Thank you you info :" + user_name + ";" + user_password + ";" + user_full_name + ";"
        # +phone_number + ";" + email)
        save_accounts(create_account(user_account_name,user_account_user,user_account_password))
        
        print('\n')
        print(f"New User {user_account_name} {user_account_user} Created")

    elif options == 'ag':
        print("Please enter your user name or create new one")
        name=input()
        account_user=find_account(name)        
        print(account_user)

        print("Generating password for you")
        autoPassword=id_generator()
        print("Your new Password Gemereated is: " + autoPassword)
        print("To save you account please enter which application you use it:")
        account_user_name = input()
        print("Saving account credentials...")
        save_accounts(create_account(account_user_name,account_user,autoPassword))

    elif options == 'cg':
        print("Put your own custom password")
        input()
        customPassword=input("Enter Your Favorite Password")
    elif options == 'dc':
        print("Displaying Credential accounts")
        if display_accounts():
                print("Here is a list of all your credential accounts")
                print('\n')

                for account in display_accounts():
                        print(f"{account.user_account_name } {account.user_account_user} .....{account.user_account_password}")

                print('\n')
    elif options == 'rc':
        print("Deleting Credential")

    elif options == 'q':
        print("Quiting the app")
        break
    else:
        print("Invalid option, bye")
        break


    # print("For old user => ou - For new User => nu - Display users => du \
    # - To Find a User => fu - Create Credentials => cc - To Quit => qu")
    # print("*"*116)
    # short_code = input().lower()
    # if short_code == 'eu':
    #     user_name = input("Enter User Name")
    #     user_password = input("Enter USer Password")

    #     # Open user file as read only

    # elif short_code == 'nu':

    # elif short_code == "du":
    #     if display_users():
    #         print("Here is a list of all your contacts")
    #         print('\n')
    #         for user in display_users():
    #             print(f"{user.user_name} {user.user_full_name} .....{user.phone_number}")
    #             print('\n')
    #     else:
    #         print('\n')
    #         print("Sorry no users")

    # elif short_code == "qu":
    #     print("Thanks")

    #     break
    # else:
    #     print("Bad option, bye")
 

if __name__ == '__main__':

    main()
