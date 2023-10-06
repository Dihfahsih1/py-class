import shutil
count_words = 0
with open("user_write.txt", "r") as file:
    data = file.read()

    count_words = len(data)

    print(count_words)