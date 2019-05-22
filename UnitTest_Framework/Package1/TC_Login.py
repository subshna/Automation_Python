import unittest

class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print ('Login By email')
        self.assertTrue(True)

    def test_loginByFB(self):
        print ('Login By FB')
        self.assertTrue(True)

    def test_loginBytwitter(self):
        print ('Login By Twitter')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()