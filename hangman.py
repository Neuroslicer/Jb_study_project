import random

print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']
c_c = random.choice(words)
length = len(c_c)
user_tries = 8
z = list(c_c.replace(c_c, '-' * length))
user_guesses = []
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        while user_tries > 0:
            x = input(f"""\n{''.join(z)}\nInput a letter: """)
            if x.islower() is False and len(x) == 1:
                print("Please enter a lowercase English letter")
            elif x.isalpha() is False and len(x) == 1:
                print("Please enter a lowercase English letter")
            elif len(x) > 1:
                print("You should input a single letter")
            else:
                if x in c_c and x not in user_guesses:
                    for y in range(length):
                        if x == c_c[y]:
                            z[y] = x
                elif x in user_guesses:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    user_tries -= 1
                user_guesses.append(x)
        else:
            if c_c == ''.join(z):
                print("You guessed the word!")
                print("You survived!")
            else:
                print("You lost!")
    elif choice == 'exit':
        break
    else:
        continue

