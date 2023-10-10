with open('data.txt', 'r') as data_file:
    with open('output.txt', 'a') as output_file:
        for line in data_file:
            output_file.write(line.upper())