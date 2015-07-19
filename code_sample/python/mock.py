import unittest
from unittest.mock import Mock

class Mailer:
    def send_email(self, email, message):
        raise NotImplementedError("Not implemented yet")

class DB:
    def insert_user(self, user):
        raise NotImplementedError("Not implemented yet")

class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name


def registerUser(email, name, db, mailer):
    user = User(email, name)
    db.insert_user(user)
    mailer.send_email(usr.email, "Good bye")

    return user

class MockTest(unittest.TestCase):
    TEST_EMAIL = 'student@campus.uib.es'
    TEST_NAME  = 'Student'

    def testRegisterUser(self):
        user = registerUser(self.TEST_EMAIL, self.TEST_NAME, DB(), Mailer())

        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.TEST_EMAIL)
        self.assertEqual(user.name, self.TEST_NAME)

if __name__ == '__main__':
    unittest.main()
