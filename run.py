#!/usr/bin/env python3.6
from user import User

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
    contact.delete_user()

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

