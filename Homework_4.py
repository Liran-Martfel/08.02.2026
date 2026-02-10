sentences = ["Hello world", "python is fun", "i love coding"]
all_word = []
for word in sentences:
    all_word.extend(word.split())
print(all_word, end=" ")

