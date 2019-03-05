# -*- coding: utf-8 -*-
import re

word_list = []
with open('E:/GitHub/python_learning/from.txt', encoding='utf-8') as words:
    words_lines = words.read()
print(words_lines)
print(type(words_lines))
pattern = re.compile(r'[A-z]+')
result = re.findall(pattern, words_lines)
print(result)
