def Position_Of_Letters(word):
    word = word.lower()
    positions = []
    for letter in word:
        if letter.isalpha():
            position = ord(letter) - ord('a') + 1
            positions.append((letter, position))
        else:
            positions.append((letter, 'Not a letter'))
    return positions