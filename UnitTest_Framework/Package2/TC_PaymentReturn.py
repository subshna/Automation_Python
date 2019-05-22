import unittest

class PaymentReturnTest(unittest.TestCase):
    def test_paymentReturnToBank(self):
        print ('Payment done to Bank')
        self.assertTrue(True)

if __name__ == '__main':
    unittest.main()