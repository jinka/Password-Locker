import pyperclip

# User Class
class User: # Class for all User Information
    """
    Class that generates new instances of users.
    """

    # Empty user list
    user_list = []

    #1
    def __init__(self,user_name,user_password,user_full_name,phone_number,email):

        """
        Class that generates new instances of users.
        """

        self.user_name = user_name
        self.user_password = user_password
        self.user_full_name = user_full_name
        self.phone_number = phone_number
        self.email = email

    #2
    def save_user(self):

        '''
        save_user method saves users objects into user_list
        '''

        User.user_list.append(self)


    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            User of person that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a contact exists from the user list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    # @classmethod
    # def copy_email(cls,number):
    #     user_found = User.find_by_number(number)
    #     pyperclip.copy(user_found.email)


class Credentials: # CLass for all Credentials
    """
    Class that generates new instances of Credentials accounts.
    """
    #EMpty Credentials list
    credentials_list = []

    def __init__(self,user_credential_name,user_credential_password,user_credential_application_name):    
        """
        Class that generates new instances of users.
        """
        self.user_credential_name = user_credential_name
        self.user_credential_password = user_credential_password
        self.user_credential_application_name = user_credential_application_name 
