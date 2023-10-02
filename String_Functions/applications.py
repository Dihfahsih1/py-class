def main():
    # Input text from the user
    input_text = input("Enter a piece of text: ")

    # Task 1: Count the number of words
    word_count = len(input_text.split())
    print(f"Number of words in the text: {word_count}")

    # Task 2: Replace a specific word
    old_word = input("Enter a word to replace: ")
    new_word = input("Enter the replacement word: ")
    replaced_text = input_text.replace(old_word, new_word)
    print("Replaced Text:")
    print(replaced_text)

    # Task 3: Find the index of a word
    search_word = input("Enter a word to find: ")
    index = input_text.find(search_word)
    if index != -1:
        print(f"The word '{search_word}' starts at index {index}.")
    else:
        print(f"The word '{search_word}' was not found.")

    # Task 4: Split the text into sentences
    sentences = input_text.split('.')
    print("Sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence.strip()}")

    # Task 5: Join the sentences back into a single paragraph
    joined_text = '. '.join(sentences)
    print("Joined Text:")
    print(joined_text)

if __name__ == "__main__":
    main()
