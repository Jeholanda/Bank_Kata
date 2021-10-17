import unittest
from US3.Bank_US3 import read_accounts


class BankTests(unittest.TestCase):

    def test_read_accounts(self):
        with open(read_accounts('tests/files/test_cases.txt')) as f:
            content = f.read()
            self.assertEqual(content, '000000000\n'
                                      '111111111 ERR\n'
                                      '222222222 ERR\n'
                                      '333333333 ERR\n'
                                      '444444444 ERR\n'
                                      '555555555 ERR\n'
                                      '666666666 ERR\n'
                                      '777777777 ERR\n'
                                      '888888888 ERR\n'
                                      '999999999 ERR\n'
                                      '123456789\n'
                                      '234567890 ERR\n'
                                      '834257998\n'
                                      '324951090 ERR\n'
                                      '098765432 ERR\n'
                                      '987654321 ERR\n'
                                      '345882865\n'
                                      '200000000 ERR\n'
                                      '490067715 ERR\n'
                                      '664371495 ERR\n')

    def test_read_ill_accounts(self):
        with open(read_accounts('tests/files/ill_test_cases.txt')) as f:
            content = f.read()
            self.assertEqual(content, '000000000\n'
                                      '111111111 ERR\n'
                                      '222222222 ERR\n'
                                      '333333333 ERR\n'
                                      '444444444 ERR\n'
                                      '555555555 ERR\n'
                                      '666666666 ERR\n'
                                      '777777777 ERR\n'
                                      '888888888 ERR\n'
                                      '999999999 ERR\n'
                                      '123456789\n'
                                      '234567890 ERR\n'
                                      '834257998\n'
                                      '324951090 ERR\n'
                                      '098765432 ERR\n'
                                      '987654321 ERR\n'
                                      '345882865\n'
                                      '200000000 ERR\n'
                                      '490067715 ERR\n'
                                      '987?5?321 ILL\n'
                                      '??7654?27 ILL\n'
                                      '12?45?78? ILL\n'
                                      '664371495 ERR\n'
                                      '86110??36 ILL\n'
                                      '0?0000051 ILL\n')

    def test_file_not_found(self):
        self.assertEqual(
            read_accounts('tests/files/fake_file.txt'), 'File "tests/files/fake_file.txt" not found.'
        )


if __name__ == '__main__':
    unittest.main()
