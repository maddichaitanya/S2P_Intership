def frequency(s):
    freq = [0] * 26  # only 26 letters (a-z)
    for ch in s:

        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)   # example: 'A'(65) → 'a'(97)

        if 'a' <= ch <= 'z':  # only count alphabets
            index = ord(ch) - 97
            freq[index] += 1

    for i in range(26):
        if freq[i] != 0:
            print(chr(i + 97), ":", freq[i])

s = "ProGramMing Is Fun"
frequency(s)
