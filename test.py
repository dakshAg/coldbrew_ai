def split_string(input_str):
    # Split the string into words
    words = input_str.split()

    # Iterate over the words and remove any spaces before uppercase letters
    for i in range(len(words)):
        word = words[i]
        new_word = ""
        for j in range(len(word)):
            if j > 0 and word[j].isupper() and word[j-1] == " ":
                # If the current character is uppercase and the previous character is a space, skip the space
                continue
            else:
                # Otherwise, add the current character to the new word
                new_word += word[j]
        # Replace the original word with the new word
        words[i] = new_word

    # Join the words back into a single string
    output_str = "".join(words)

    # Print the output string
    return output_str
