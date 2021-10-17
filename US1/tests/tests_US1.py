import unittest
from US1.Bank_US1 import read_accounts


class BankTests(unittest.TestCase):

    def test_read_accounts(self):
        self.assertEqual(
            read_accounts('tests/files/test_cases.txt'), [
                '000000000',
                '111111111',
                '222222222',
                '333333333',
                '444444444',
                '555555555',
                '666666666',
                '777777777',
                '888888888',
                '999999999',
                '123456789',
                '234567890',
                '834257998',
                '324951090',
                '098765432',
                '987654321',
                '345882865',
                '200000000',
                '490067715',
                '664371495'
            ]
        )

    def test_file_not_found(self):
        self.assertEqual(
            read_accounts('tests/files/fake_file.txt'), 'File "tests/files/fake_file.txt" not found.'
        )


if __name__ == '__main__':
    unittest.main()
