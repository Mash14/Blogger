import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'Marky',email = 'mark1@gmail.com',password = 'potato')

    def test_instance(self):
        '''
        testcase to acertain self.new_user is an instance of User model
        '''
        self.assertTrue(isinstance(self.new_user,User))

    def test_password_setter(self):
        '''
        testcase test_password_setter this ascertains that when password is being hashed and the pass_secure contains a value
        '''
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        '''
        confirms that our application raises an AttributeError when we try and access the password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        test confirms that our password_hash can be verified when we pass in the correct password
        '''
        self.assertTrue(self.new_user.verify_password('potato'))