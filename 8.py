def reverse_and_remove_duplicates(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Remove duplicates while preserving the order
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Reverse the order of words
    reversed_sentence = ' '.join(unique_words[::-1])
    return reversed_sentence

# Input sentence
input_sentence = "I have a car"

# Process the input and print the output
output_sentence = reverse_and_remove_duplicates(input_sentence)
print("Input:", input_sentence)
print("Output:", output_sentence)
