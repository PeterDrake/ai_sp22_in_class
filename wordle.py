word = 'knoll'

for i in range(6):
    guess = input('Your guess: ')
    # Find letters in word that were not perfectly guessed
    imperfect = ''
    for j in range(5):
        if not word[j] == guess[j]:
            imperfect += word[j]
    # Generate clue response
    clue = ''
    for j in range(5):
        if word[j] == guess[j]:
            clue += '!'
        elif guess[j] in imperfect:
            clue += '?'
            imperfect = imperfect.replace(guess[j], '', 1)
        else:
            clue += '.'
    print(clue)
    if clue == '!!!!!':
        exit()

print("You're out of guesses. The word was:", word)
