def capitalize_first_letter(wrd):
	return wrd[0].upper() + wrd[1:].lower()

with open('data.txt', 'r') as data_file:
	with open('output.txt', 'a') as output_file:
		for line in data_file:
			word_list = line.split()
			word_list = [capitalize_first_letter(word) for word in word_list]
			output_file.write(" ".join(word_list) + "\n")
