word = 'knoll'
guess = input('Your guess: ')

# Find letters in word that were not perfectly guessed
imperfect = ''
for i in range(5):
    if word[i] == guess[i]:
        pass
    else:
        imperfect += word[i]
print(imperfect)

# Generate clue response
correct = ''
for i in range(5):
    if word[i] == guess[i]:
        correct += '!'
    elif guess[i] in imperfect:
        correct += '?'
        imperfect = imperfect.replace(guess[i], '', 1)
    else:
        correct += '.'

print(correct)
