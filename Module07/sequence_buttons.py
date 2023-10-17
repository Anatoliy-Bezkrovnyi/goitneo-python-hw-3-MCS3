def sequence_buttons(string):
    NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    LETTERS = (".,?!:", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz", " ")

    TRANS_DICT = {}

    prep_string = string.lower()

    for eng, code in zip(LETTERS, NUMBERS):
        for idx, ch in enumerate(eng, 1):
            TRANS_DICT[ord(ch)] = code * idx

    translate = prep_string.translate(TRANS_DICT)

    return translate


string = "Hello"
print(sequence_buttons(string))