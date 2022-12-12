def get_hapaxes(filename):
  # Open the file and read its contents into a string
  with open(filename, 'r') as file:
    text = file.read()

  # Split the string into a list of words
  words = text.split(' ')

  # Create a dictionary to count the occurrences of each word
  word_counts = {}
  for word in words:
    # Ignore capitalization by converting all words to lowercase
    word = word.lower()

    # If the word is not in the dictionary, add it with a count of 1
    if word not in word_counts:
      word_counts[word] = 1
    # Otherwise, increment the count for that word
    else:
      word_counts[word] += 1

  # Create a list of hapaxes
  hapaxes = []
  for word, count in word_counts.items():
    # If a word has a count of 1, it is a hapax
    if count == 1:
      hapaxes.append(word)

  # Return the list of hapaxes
  return hapaxes
filename = 'filename.txt'
hapaxes = get_hapaxes(filename)
print(hapaxes)





