def nth_char(index, string):
    try:
        output = string[index]
        return output
    except:
        return None


def nth_word(index, string):
    try:
        words = string.split()
        return words[index]
    except:
        return None


def nth_of_mth(n, m, string):
    try:
        words = string.split()
        word = words[m]
        char = word[n]
        print("Character", n, "of word", m, "is", char)
    except:
        print("Oops!")

