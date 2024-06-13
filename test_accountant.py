import unittest
from accountant import Accountant

class TestAccountant(unittest.TestCase):
    """Tests for the class Accountant."""

    def test_initial_balance(self):
        # Test with default balance
        acc = Accountant()
        self.assertEqual(acc.balance, 0)

        # Test with specified balance
        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)

    def test_deposit(self):
        acc = Accountant()
        acc.deposit(100)
        self.assertEqual(acc.balance, 100)


    def test_withdraw(self):
        acc = Accountant(balance=200)
        acc.withdraw(50)
        self.assertEqual(acc.balance, 150)

        # Test withdrawing more than the balance
        '''
                with self.assertRaises(ValueError):
            acc.withdraw(300)
        '''

    def test_withdrawal(self):
        # Test single withdrawal.
        self.acc.deposit(1000)
        self.acc.withdraw(100)
        self.assertEqual(self.acc.balance, 900)

if __name__ == '__main__':
    unittest.main()
