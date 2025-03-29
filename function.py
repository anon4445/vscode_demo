def combine_words(first, last):
    combined_words = first + " " + last
    return combined_words

first_word = "something"
last_word = "else"
result = combine_words(first_word, last_word)
print(result)

first_word = "nothing"
result = combine_words(first_word, last_word)
print(result)