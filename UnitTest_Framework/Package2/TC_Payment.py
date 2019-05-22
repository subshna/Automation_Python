import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print ('Payment has to be done in dollars')
        self.assertTrue(True)

    def test_paymentInRupee(self):
        print ('Payment has to be done in Rupee')
        self.assertTrue(True)

if __name__ == '__main':
    unittest.main()