word = 'knoll'

guess = input('Your guess: ')

correct = ''
for i in range(5):
    if word[i] == guess[i]:
        correct += '!'
    elif guess[i] in word:
        correct += '?'
    else:
        correct += '.'

print(correct)
