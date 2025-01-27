#создаю лист
lst = ['Tell', 'me', 'what', 'must', 'I', 'do', 'Cause', 'luckily',
       'I', 'm', 'good', 'at', 'reading']
#получаю индексы листа, с помощью for
dic = {}
for index, word in enumerate(lst, start=1):
    dic[index] = word

print(dic)
