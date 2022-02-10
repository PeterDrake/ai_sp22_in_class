def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) < len(longest):
            longest = word
    return longest


def mph2fpf(x):
    '''
    Converts miles per hour to furlongs per fortnight.
    '''
    return x * 2688


def longest_word(words):
    return max(words, key=len)


def multiple_return():
    return 1, 2
