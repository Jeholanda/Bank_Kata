import unittest
from US2.Bank_US2 import read_accounts


class BankTests(unittest.TestCase):

    def test_read_accounts(self):
        self.assertEqual(
            read_accounts('tests/files/test_cases.txt'), [
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                False,
                False
            ]
        )

    def test_file_not_found(self):
        self.assertEqual(
            read_accounts('tests/files/fake_file.txt'), 'File "tests/files/fake_file.txt" not found.'
        )


if __name__ == '__main__':
    unittest.main()
