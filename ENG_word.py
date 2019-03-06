# -*- coding: utf-8 -*-
import re

word_list = []
with open('E:/GitHub/python_learning/txt/from.txt', encoding='utf-8') as words:
    words_lines = words.read()
# print(words_lines)
# print(type(words_lines))
pattern = re.compile(r'[A-z]+')
result = re.findall(pattern, words_lines)
# print(result)
result_final = sorted(result, key=lambda x: x[0].lower())
print(result_final)

export_word = '\n'.join(result_final)
# print(export_word)
with open('E:/GitHub/python_learning/txt/to.txt', 'w', encoding='utf-8') as word_write:
    word_write.write(export_word)
