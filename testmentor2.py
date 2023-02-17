from collections import defaultdict
test_list = input('Введите предложение - ')
print("Предложение: " + str(test_list))
temp = defaultdict(int)
for wrd in test_list.split(' '):
    temp[wrd] += 1
res = max(temp, key=temp.get)
print("Чаще всего встречается: " + str(res))