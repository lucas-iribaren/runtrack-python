def chaine_inverse(text):
    string = ""
    i = len(text)-1
    while (i >= 0):
        string += text[i]
        i -= 1
    return string
print(chaine_inverse("nikana"))

def bis(x):
    res = ''
    for k in range(len(x)-1, -1, -1):
        res += x[k]
    return res

print(bis("live"))

def bis2(y):
    return y[::-1]
print(bis2("stressed")) 