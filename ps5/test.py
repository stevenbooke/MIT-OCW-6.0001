import string
def is_phrase_in(phrase, text):
    parsed_phrase = ''.join(phrase.split()).lower() #remove all spaces in phrase and make it lowercase
    pasrsed_text = ''
    for c in text:
        if c not in string.punctuation: # remove punctuations and spaces from text and then make it lowercase
            pasrsed_text += c
    pasrsed_text = ''.join(pasrsed_text.split()).lower()
    if parsed_phrase in pasrsed_text:
        return True
    else:
        return False

phrase = input('Enter a phrase')
text = input('Enter some text')

print(is_phrase_in(phrase, text))
