def formatting():
    # The curry brackets represent placeholders
    say = "Hello! {} name is {} and I am {} years old."
    # We provide our values when formatting the string depending on the number of strings
    # when formatting, we can provide our values using different datatypes.
    print(say.format("My", "Alvin", 20))
formatting()
# if you provide less values it will return an error message.