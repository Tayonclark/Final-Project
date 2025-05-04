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


def score(word):
    position_list = Position_Of_Letters(word)
    final_score = 0

    for letter, position in position_list:
        # checks if position is an intiger (some items in position are "Not a letter")
        if isinstance(position, int):
            final_score += position
    return final_score


if __name__ == "__main__":
    user_input = input("Enter a word or phrase to see total score: ")
    
    total_score = score(user_input)
    print( f'Total score of input: {total_score}')



