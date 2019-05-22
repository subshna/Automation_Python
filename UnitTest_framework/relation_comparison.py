import unittest

class Test(unittest.TestCase):
    def test_name1(self):
        self.assertGreater(100, 10)

    def test_name2(self):
        self.assertGreaterEqual(10, 10)

    def test_name3(self):
        self.assertLess(10, 100)

    def test_name4(self):
        self.assertLessEqual(100, 100)

if __name__ == '__main__':
    unittest.main()