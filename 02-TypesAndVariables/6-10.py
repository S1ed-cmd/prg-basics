movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Big letters: ', movie.upper())

# print title in small letters
print('Small letters:',movie. lower())

# print how many times the vowel "e" appears in the title
e_count = movie.lower().count('e')
print('how many letters e', e_count)

# print where in the text is the word "Lord"
Lord_finder = movie.find("Lord")
print('where is Lord', Lord_finder)
# print where in the text is the word "dragon"
Dragon = movie.find("Dragon")
print('where is dragon', Dragon)