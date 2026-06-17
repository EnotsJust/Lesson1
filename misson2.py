import re
file = open("Lesson1\\text.txt", mode='r',encoding='utf-8')
content = file.read()
print(content)
words = re.findall(r'\w+', content)
dic = {}
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
for word in dic:
    print(word, dic[word])
file.close()