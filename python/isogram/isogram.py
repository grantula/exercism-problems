def is_isogram(string):
    d = {}
    for x in string:
        if x.isalpha():
            x = x.lower()
            if x in d.keys():
                return False
            d[x] = 0
    return True
