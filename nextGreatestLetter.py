def nextGreatestLetter(letters, target):
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]

print(nextGreatestLetter(["b","c"],"a"))
