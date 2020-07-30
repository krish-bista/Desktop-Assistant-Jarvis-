import random
possible_ans = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']
secret_letter = random.choice(possible_ans)
guess_count = 0
max_guess = 5
while guess_count < max_guess:
    user = input('Guess : ')
    guess_count += 1
    if user == secret_letter:
        print('Correct You won !')
        print(f"You took {guess_count} guesses to win")
        break
    elif user != secret_letter:
        print('Incorrect!')
        print(f'No. of guess left = {max_guess - guess_count}')
else:
    print('Game over....\n secret letter was', secret_letter )
