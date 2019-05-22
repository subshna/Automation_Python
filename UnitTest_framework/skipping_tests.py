import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print ('This is search test')

    @unittest.skip('test_advancesearch - This test is under development')
    def test_advancesearch(self):
        print('This is advance search test')

    @unittest.skipIf(1==1, 'Condition is True')
    def test_prepaid(self):
        print('This is pre-paid test')

    def test_postpaid(self):
        print('This is post-paid test')

    def test_loginbygmail(self):
        print('This is login by Gmail account')

    def test_loginbytwitter(self):
        print('This is login by Twitter account')

if __name__ == '__main__':
    unittest.main()