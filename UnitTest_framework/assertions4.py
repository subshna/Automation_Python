import unittest

class Test(unittest.TestCase):
    def test_name1(self):
        lst = ['Python', 'Java', 'Go', 'Ruby']

        self.assertIn('Python', lst, 'String Found')

    def test_name2(self):
        lst = ['Python', 'Java', 'Go', 'Ruby']

        self.assertNotIn('Scala', lst)

if __name__ == '__main__':
    unittest.main()