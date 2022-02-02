import random
word = 'knoll'

legal_words = []
with open('legal_words.txt') as f:
    for line in f:
        legal_words.append(line.strip())

mystery_words = []
with open('mystery.txt') as f:
    for line in f:
        mystery_words.append(line.strip())

word = random.choice(mystery_words)

i=0
while i < 6:
    i+=1
    guess = input('Your guess: ')
    if not guess in legal_words:
        print("That's not a legal word")
        i-=1
        continue
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
