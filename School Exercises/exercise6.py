def count_word(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

input_sentence = input("Enter a sentence : ")
result = count_word(input_sentence)
print("The sentence is : ", input_sentence)
print("The word count is : ",result)