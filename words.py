
def print_upper_words(words, letters = []):
    """Accepts a list of words(strings) and an optional list of letters(strings).
       -If no letters are passed each word is verified as a string and printed in upper case
       -If letters are passed the function will only print words that start with an included letter
    """

    if len(letters) > 0:
        for letter in letters:
            if type(letter) == str:
                for word in words:
                    if type(word) == str:
                        if word.upper().startswith(letter.upper()):
                            print(word.upper())                                       
             
    else:
        for word in words:
            if type(word) == str:
                print(word.upper())

print_upper_words(['hello', 'goodbye', 'welcome'], ['h', 'w', 'j'])