import re
# get key words list from file without useless blank space
with open('E:/Python_folder/words.txt') as words:
    words_db = words.read().replace(' ', '').split('\n')
key_words = []
for i in range(0, len(words_db)):  # remove useless enter in txt file
        if words_db[i] != '':
            key_words.append(words_db[i])
print(key_words)


# replace keywords letter and return replaced keyword
def word_replace(word):
    if len(word) == 1:
        replaced = '*'
    else:
        replaced = word.replace(word[1:], (len(word)-1)*'*')
    return replaced


# split sentence include punctuation
user_input = re.split(r'(\w+)', input('Please input a sentence:'))
for j in range(0, len(user_input)):
    if user_input[j] in key_words:
        user_input[j] = word_replace(user_input[j])
        replaced_word = ''.join(user_input)
    else:
        replaced_word = ''.join(user_input)
print(replaced_word)
