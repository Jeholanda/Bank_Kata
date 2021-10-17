from helper import NUMBERS, FAILED_NUMBERS
import os


def read_accounts(file: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path, file)
    output_file = f'{file_name[:-4]}_output.txt'

    try:
        with open(file_name) as f, open(output_file, 'w') as out:
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
                            else:
                                account += '?'

                        # validate account
                        if '?' in account:
                            out.write(f'{find_illegible_account(account)}\n')
                        else:
                            if check_sum(account):
                                out.write(f'{account}\n')
                            else:
                                out.write(f'{find_account(account)}\n')

                        # restart list
                        parts = []
                    else:
                        parts.append(['   '] * 9)
        return output_file

    except FileNotFoundError:
        return f'File "{file}" not found.'


def check_sum(account):
    # invert and convert elements to int
    acc = list(account[::-1])
    chk = [(i + 1) * int(acc[i]) for i in range(len(acc))]

    if sum(chk) % 11 == 0:
        return True
    return False


def find_account(account):
    accounts = []

    for i, n in enumerate(account):
        if int(n) in FAILED_NUMBERS.keys():
            for x in FAILED_NUMBERS[int(n)]:
                temp = list(account)
                temp[i] = str(x)
                acc = ''.join(temp)
                if check_sum(acc):
                    # return AMB if I have more than one possible account
                    if len(accounts) > 0:
                        return f'{account} AMB'
                    else:
                        accounts.append(acc)

    if len(accounts) == 1:
        return f'{accounts[0]}'
    else:
        return f'{account} ILL'


def find_illegible_account(account):
    accounts = []
    cnt = 0

    while cnt < 10:
        acc = account.replace('?', str(cnt))
        if check_sum(acc):
            # return AMB if I have more than one possible account
            if len(accounts) > 0:
                return f'{account} AMB'
            else:
                accounts.append(acc)
        cnt += 1

    if len(accounts) == 1:
        return f'{accounts[0]}'
    else:
        return f'{account} ILL'


if __name__ == '__main__':
    print(read_accounts('tests/files/test_cases.txt'))
    print(read_accounts('tests/files/ill_test_cases.txt'))
    
