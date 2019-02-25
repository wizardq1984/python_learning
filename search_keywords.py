import os

keyword = input('Please input the keyword:')
file_dir = input('Please input the dir which you want to search:')
founded = []
for url, folder, files in os.walk(file_dir):
    for file in files:
        full_url = url + '/' + file
        if keyword in file:
            founded.append(full_url)
            with open(full_url) as file_text:
                for text_lines in file_text.readlines():
                    if keyword in text_lines:
                        founded.append(full_url+':'+text_lines)
print(founded)
for search_result in founded:
    if '\n' in search_result:
        search_result = search_result.replace('\n', '')
        print(search_result)
    else:
        print(search_result)
