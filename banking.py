import random
import sys
import sqlite3


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("""CREATE TABLE if not exists card (id integer primary key autoincrement, 
               number text, pin text, balance integer default 0)""")
conn.commit()
card_numbers_created = []
card_pins = []

while True:
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    user_input = input()

    if user_input == '1':
        user_card_number = str(random.random())
        user_card_number = '400000' + user_card_number.replace(user_card_number, user_card_number[2:11])
        user_card_number_list = list(user_card_number)
        for i in range(0, 15):
            user_card_number_list[i] = int(user_card_number_list[i])
            if i % 2 == 0:
                user_card_number_list[i] *= 2
                if user_card_number_list[i] > 9:
                    user_card_number_list[i] -= 9
        sum_list = sum(user_card_number_list)
        if sum_list % 10 != 0:
            user_card_number += str(10 - sum_list % 10)
        else:
            user_card_number += '0'
        user_pin = str(random.random())
        user_pin = user_pin.replace(user_pin, user_pin[2:6])
        cur.execute("INSERT INTO card(number, pin) VALUES ({}, {})".format(user_card_number, user_pin))
        conn.commit()
        print('Your card number has been created')
        print('Your card number:')
        print(user_card_number)
        card_numbers_created.append(user_card_number)
        print('Your card PIN:')
        print(f'{user_pin}\n')
        card_pins.append(user_pin)
    elif user_input == '2':
        print('Enter your card number:')
        card_number_input = input()
        print('Enter your PIN:')
        pin_input = input()
        if card_number_input in card_numbers_created and pin_input in card_pins:
            card_index = card_numbers_created.index(card_number_input)
            if pin_input == card_pins[card_index]:
                print('\nYou have successfully logged in!\n')
                while True:
                    print('1. Balance')
                    print('2. Add income')
                    print('3. Do transfer')
                    print('4. Close account')
                    print('5. Log out')
                    print('0. Exit')
                    logged_user_input = input()
                    if logged_user_input == '1':
                        cur.execute('SELECT balance FROM card WHERE number={}'.format(card_number_input))
                        balance = cur.fetchone()
                        print('\nBalance: ', balance[0], '\n')
                    elif logged_user_input == '2':
                        print('Enter income:')
                        income_input = input()
                        cur.execute('SELECT balance FROM card WHERE number={}'.format(card_number_input))
                        balance = cur.fetchone()
                        new_balance = str(int(balance[0]) + int(income_input))
                        cur.execute('UPDATE card SET balance={} WHERE number={}'.format(new_balance, card_number_input))
                        conn.commit()
                        print('Income was added!\n')
                    elif logged_user_input == '3':
                        print('Transfer')
                        print('Enter card number:')
                        card_number_transfer = input()

                        def check_luhn(card_no):
                            n_digits = len(card_no)
                            n_sum = 0
                            is_second = False
                            for n in range(n_digits - 1, -1, -1):
                                d = ord(card_no[n]) - ord('0')
                                if is_second is True:
                                    d = d * 2
                                n_sum += d // 10
                                n_sum += d % 10
                                is_second = not is_second
                            if n_sum % 10 == 0:
                                return True
                            else:
                                return False
                        if check_luhn(card_number_transfer) is False:
                            print('Probably you made a mistake in the card number. Please try again!\n')
                        else:
                            cur.execute("SELECT number FROM card WHERE number={}".format(card_number_transfer))
                            s = cur.fetchone()
                            if s is None or s[0] != card_number_transfer:
                                print('Such a card does not exist.\n')
                            elif s[0] == card_number_transfer and card_number_transfer != card_number_input:
                                print('Enter how much money you want to transfer:')
                                money_transfer = input()
                                cur.execute('SELECT balance FROM card WHERE number={}'.format(card_number_input))
                                balance = cur.fetchone()
                                if int(money_transfer) > balance[0]:
                                    print('Not enough money!\n')
                                else:
                                    cur.execute('SELECT balance FROM card WHERE number={}'.format(card_number_input))
                                    balance = cur.fetchone()
                                    new_balance = str(int(balance[0]) - int(money_transfer))
                                    cur.execute('UPDATE card SET balance={} WHERE number={}'.format(new_balance,
                                                                                                    card_number_input))
                                    cur.execute('SELECT balance FROM card WHERE number={}'.format(card_number_transfer))
                                    balance = cur.fetchone()
                                    new_balance = str(int(balance[0]) + int(money_transfer))
                                    cur.execute('UPDATE card SET balance={} WHERE number={}'
                                                .format(new_balance, card_number_transfer))
                                    conn.commit()
                                    print('Success!\n')
                            else:
                                print('You can\'t transfer money to the same account!\n')
                    elif logged_user_input == '4':
                        cur.execute('DELETE FROM card WHERE number={}'.format(card_number_input))
                        conn.commit()
                        print('\nThe account has been closed!\n')
                    elif logged_user_input == '5':
                        print('You have successfully logged out!\n')
                        break
                    elif logged_user_input == '0':
                        print('\nBye!')
                        sys.exit()
            else:
                print('\nWrong card number or PIN!\n')
        else:
            print('\nWrong card number or PIN!\n')

    elif user_input == '0':
        print('\nBye!')
        break

conn.commit()
conn.close()
