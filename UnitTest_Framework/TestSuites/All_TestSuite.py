import unittest
from Package1.TC_Login import LoginTest
from Package1.TC_Signup import SignupTest

from Package2.TC_Payment import PaymentTest
from Package2.TC_PaymentReturn import PaymentReturnTest

# Get all the Testcases from Packages
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# Creating TestSuites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

# To Run the Test Suite
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)