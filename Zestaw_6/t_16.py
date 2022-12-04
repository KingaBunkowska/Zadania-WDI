def vowels(s):
    res = 0
    for i in range(0, len(s)):
        if s[i] in ('a', 'e', 'i', 'o', 'u', 'y'):
            res += 1

    return res


def weight(s):
    res = 0
    for i in range(len(s)):
        res += ord(s[i])

    return res


def without_i(s, i):
    res = s[:i] + s[i+1:]
    return res


def make_words(vowel, value, s, i=0):
    global flag
    if s=="ula": print("AAAAAA")
    if vowels(s) == vowel and weight(s) == value:
        flag = 1
        return s
    elif i >= len(s):
        return "1"
    elif flag==1:
        return ""
    else:
        return max(make_words(vowel, value, without_i(s, i), i), make_words(vowel, value, s, i+1))


def words(s1, s2):
    vowel = vowels(s1)

    if vowels(s2) < vowel:
        return 0

    value = weight(s1)

    if weight(s2) < value:
        return 0

    x =  make_words(vowel, value, s2)

    if x == "0":
        return 0

    return x


flag = 0
print(words("exe", "aorighw"))