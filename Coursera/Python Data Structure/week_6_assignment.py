file_handle = open('mbox-short.txt')
file_read = file_handle.read()
splitting = file_read.split()
# print(file_read)
list1, list2 = list(), list()

for i in range(len(splitting[:])):
    if splitting[i] == 'From':
        list1 = splitting[i+5].split(":")
        list2.append(list1[0])
    else:
        continue
# print(list2)
dictionary = dict()
for i in list2:
    dictionary[i] = dictionary.get(i, 0)+1
list3 = sorted(dictionary.items())
for i in list3:
    print(i[0], i[1])
