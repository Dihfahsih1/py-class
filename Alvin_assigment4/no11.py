def string_len():
    text = ["What's your name?",
            "how old are you?",
            "Avindez"]
    # Create an empty list for the lengths of each string in the list
    str_len = []
    for a in text:
        # Append the empty list to each length of the strings in the text list
        str_len.append(len(a))
        # Then print the list containing each string length
        print(str_len)
string_len()