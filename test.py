#make test cases for wallet.py

import unittest
from wallet import Wallet

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet(50)

    def test_get_ammount(self):
        self.assertEqual(self.wallet.getAmmount(50), 50)

    def test_set_ammount(self):
        self.assertEqual(self.wallet.setAmmount(150), 150)

    def test_remove_ammount(self):
        self.assertEqual(self.wallet.removeAmmount(), 0)
        print("hahah")

if __name__ == '__main__':
    unittest.main()
