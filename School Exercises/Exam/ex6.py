def count_word_occurrence(sentence):
    sentence = sentence.replace('.','').lower()
    words = sentence.split()
    counted_words = {}

    for i in words:
        if i in counted_words:
            counted_words[i] += 1
        else:
            counted_words[i] = 1
    return counted_words

sentence = "This is a boy. This is a girl."
result = count_word_occurrence(sentence)
print(result)