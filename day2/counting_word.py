def read_file(filename):
    try:
        f = open(filename, 'r', encoding="utf-8")
        content = f.read()
        return content
    except FileNotFoundError:
        return None

def cleaning_data(text):
    text = text.replace(',', ' ').replace('.', ' ').replace('[8]', ' ')
    text = text.lower()
    return text

result = read_file('thailand.txt')
result = cleaning_data(result)
words_list = result.split() # split => list
words_set = set(words_list) # set => unique words
for word in words_set:
    print(word)
print(len(words_list))
print(len(words_set))
