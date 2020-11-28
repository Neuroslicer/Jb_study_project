import random

f = open('rating.txt', 'r+')

rating_list = list(f)
rating_list_new = []
for i in range(len(rating_list)):
    rating_list[i] = rating_list[i].split()
    rating_list_new.extend(rating_list[i])

rating_list = rating_list_new

user_name = input('Enter your name: ')
print(f'Hello, {user_name}')
if user_name in rating_list:
    score = rating_list[rating_list.index(user_name) + 1]
else:
    score = '0'
    rating_list.append(user_name)
    rating_list.append(score)


def win_condition(x):
    global score
    n = user_list.index(x)
    x_list = user_list.copy()
    x_list = x_list * 2
    x_list = x_list[n + 1: (len(x_list) // 4 + n + 1)]
    if x == computer_choice:
        score = str(int(score) + 50)
        print(f'There is a draw ({computer_choice})')
    elif computer_choice not in x_list:
        score = str(int(score) + 100)
        print(f'Well done. The computer chose {computer_choice} and failed')
    else:
        print('Sorry, but the computer chose {}'.format(computer_choice))


game_mode = input()
if game_mode == '':
    user_list = ['scissors', 'paper', 'rock']
else:
    user_list = game_mode.split(',')
print("Okay, let's start")
while True:
    user_input = input()
    computer_choice = random.choice(user_list)
    if user_input == '!exit':
        print('Bye!')
        f.close()
        break
    elif user_input == '!rating':
        print(score)
    elif user_input in user_list:
        win_condition(user_input)
    else:
        print('Invalid input')
