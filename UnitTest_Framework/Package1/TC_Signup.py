import unittest

class SignupTest(unittest.TestCase):
    def test_SignupEmail(self):
        print ('Signup By email')
        self.assertTrue(True)

    def test_SignupByFB(self):
        print ('Signup By FB')
        self.assertTrue(True)

    def test_SignupBytwitter(self):
        print ('Signup By Twitter')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()