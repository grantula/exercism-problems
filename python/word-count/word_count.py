import re
def word_count(string):
    x = {}
    string = re.sub('[^0-9a-zA-Z]+', ' ', string.lower())
    for word in string.strip().split():
        count = x.get(word, 0) + 1
        x[word] = count
    return x
