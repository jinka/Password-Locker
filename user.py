class User:
    """
    Class that generates new instances of users
    """

    user_list = [] # Empty contact list

    def __init__(self,user_name,user_password,full_name,phone_number,email):

      # docstring removed for simplicity

        self.user_name = user_name
        self.user_password = user_password
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)
