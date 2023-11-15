interest_in_computer_science = False
like_computer_games = False
have_an_instagram_account = False

interest_in_computer_science_answer = input('Are you interested in computer science? (Y/N): ')
if interest_in_computer_science_answer == 'Y':
    interest_in_computer_science = True

like_computer_games_answer = input('Do you like playing computer games? (Y/N): ')
if like_computer_games_answer == 'Y':
    like_computer_games = True

have_an_instagram_account_answer = input('Do you have an Instagram account? (Y/N): ')
if have_an_instagram_account_answer == 'Y':
    have_an_instagram_account = True

print(f'Interested in computer science: {'Yes' if interest_in_computer_science == True else 'No'}')
print(f'Playing computer games: {'Yes' if like_computer_games == True else 'No'}')
print(f'Has an Instagram account: {'Yes' if have_an_instagram_account == True else 'No'}')