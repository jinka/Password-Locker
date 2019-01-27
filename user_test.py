import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("daud","password","Daud Mohamed","0716761606","daud@gmail.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"daud")
        self.assertEqual(self.new_user.user_password,"password")
        self.assertEqual(self.new_user.full_name,"Daud Mohamed")
        self.assertEqual(self.new_user.phone_number,"0716761606")
        self.assertEqual(self.new_user.email,"daud@gmail.com")


if __name__ == '__main__':
    unittest.main()
