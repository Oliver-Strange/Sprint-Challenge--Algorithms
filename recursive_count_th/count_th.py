'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# word.count('th', beg= 0, end=len(word))
# word.startswith('th')


def count_th(word):

    # desire = "th"
                                                        # set a count of times letter pair appears
    count = 0

    if word == "":                                      # if there is an empty string, return zero
        return 0

    if len(word) < 2:
        return 0

        # check the first letters, or where the recursion starts the string
    if word.startswith('th'):
                                                        # if 'th' is there there, set count to one
        count = 1

    if len(word) > 2:                                   # if there are more than two letters,
                                                        # start on the second character through the rest of the characters and add the count
        return count_th(word[1:len(word)]) + count

    else:                                               # once the length of the word is gone over return the count
        return count
