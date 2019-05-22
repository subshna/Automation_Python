import unittest

def setUpModule():
    print ('Setup Module')

def tearDownModule():
    print ('Teardown Module')

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print ('Login Test')

    @classmethod
    def tearDown(self):
        print ('Logout Test')

    @classmethod
    def setUpClass(cls):
        print ('Open the Application')

    @classmethod
    def tearDownClass(cls):
        print ('Close the Application')

    def test_search(self):
        print('This is search test')

    def test_advancesearch(self):
        print('This is advance search test')

    def test_prepaid(self):
        print('This is prepaid test')

    def test_postpaid(self):
        print('This is postpaid test')

if __name__ == '__main__':
    unittest.main()