import re


def find_word(text, word):
    answer = {}
    search_result = re.search(word, text)

    if not search_result:
        answer.update({
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        })
    elif search_result: 
        answer.update({
            'result': True,
            'first_index': min(search_result.span()),
            'last_index': max(search_result.span()),
            'search_string': search_result.group(),
            'string': search_result.string
        })

    return answer

 

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "python"
answer = find_word(text, word)

for key, value in answer.items():
    print(key, value)

