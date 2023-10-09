def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()    
    is_spam_words = False

    for words in spam_words:
        spam_words = words.lower()
        if not space_around:
            if spam_words in text:
                is_spam_words = True
            
        elif space_around:
            spam_word_beginning = text.find(spam_words)
            spam_word_length = len(spam_words)
            if text.startswith(spam_words):
                if (text[spam_word_beginning + spam_word_length] == " " or text[spam_word_beginning + spam_word_length] == "."):
                    is_spam_words = True
                
            elif spam_word_beginning > 0:
                try: 
                    if text[spam_word_beginning -1] == " " and (text[spam_word_beginning + spam_word_length] == " " or text[spam_word_beginning + spam_word_length] == "."):
                        is_spam_words = True
                   
                except IndexError:
                    is_spam_words = True

    return is_spam_words
            
        

text = "Мо лох чорт чи ні"
spam = ["Лох", "Чорт"]

print(is_spam_words(text, spam, space_around=True))

