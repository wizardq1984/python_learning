import re

with open('E:/GitHub/python_learning/txt/eng_news.txt', 'r') as f:
    words = f.read()
# print(words)
pattern = r'\w+'
words_list = re.findall(pattern, words)
# print(words_list)
print('There is %d words in that txt file.' % len(words_list))
