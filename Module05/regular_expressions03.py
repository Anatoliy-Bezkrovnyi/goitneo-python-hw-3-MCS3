import re


def replace_spam_words(text, spam_words):
    censored_string = text
    mask = ""

    for word in spam_words:        
        for _ in range(len(word)):
            mask = mask + "*" 
        censored_string = re.sub(word, mask, censored_string, flags=re.IGNORECASE)
        mask = ""
    return censored_string

text = "That was fucking beautiful morning in this shitty place"
spam_words = ["Fucking", "Shitty"]

print(replace_spam_words(text, spam_words))