myFile1 = open('text.txt', 'r')
lines = myFile1.readlines()

punctuation = ".","?","!"
first = ["mr.", "mrs", "jr.","ms.", "i.e."]

for line in lines:
    words = line.split()
    for word in words:
        if word.lower() in first:
            print(word + " ", end='')
        elif word[-1] in punctuation:
            print(word + "\n", end='')
        else:
            print(word + " ", end='')