punctuation = ",.?!'"
def find_words(filename):
    """
    print 3 letter words starting with b
    :param filename: the file
    :return: Nothing
    """
    with open(filename, 'r') as f:
        for line in f:

            for p in punctuation:
                line=line.replace(p, " ")

            words=line.split()
            for word in words:
                if len(word)==3 and word.upper()[0] in"Bb":
                    print(word)


find_words("input.txt")