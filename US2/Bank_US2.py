from helper import NUMBERS
import os


def read_accounts(file: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path, file)

    accounts = []

    try:
        with open(file_name) as f:
            parts = []
            for row in f:
                if row.strip():
                    parts.append([row[i:i + 3].replace('\n', '') for i in range(0, len(row), 3)])
                else:
                    """
                     If the row is blank it means two things:
                        > We are in the last row of the account block so I can decode the account and restart the
                        'parts' list for the next account block. In this case, 'parts' will always have elements. 
                     Or
                        > We have a sequence of number without 'top', so I fill the list with 3 blank spaces.
                        For example: 111111111 or 444444444
                        In this case, 'parts' will be always empty because it was restarted at the end of the previous 
                        account block.
                    """

                    if len(parts) > 0:
                        account = ''
                        # decode all 9 digits
                        for i in range(9):
                            if parts[0][i] + parts[1][i] + parts[2][i] in NUMBERS.keys():
                                account += NUMBERS[parts[0][i] + parts[1][i] + parts[2][i]]

                        # validate account by checking sum
                        accounts.append(True if checksum(account) else False)

                        # restart list
                        parts = []
                    else:
                        parts.append(['   '] * 9)
        return accounts

    except FileNotFoundError:
        return f'File "{file}" not found.'


def checksum(account):
    # invert list and convert to int
    acc = list(account[::-1])
    chk = [(i + 1) * int(acc[i]) for i in range(len(acc))]

    if sum(chk) % 11 == 0:
        return True
    return False


if __name__ == '__main__':
    print(read_accounts('tests/files/test_cases.txt'))
    
