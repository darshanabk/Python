file_handle = open('mbox-short.txt')
file_read = file_handle.read()
striping = file_read.rstrip()
splitting = striping.split()
# print(splitting)
lst = list()
for i in range(len(splitting)):
    # print(i)
    splitting[i] = splitting[i].strip()
    if splitting[i].startswith('From:'):
        lst.append(splitting[i+1])
        # print(lst)
    else:
        continue

dictionary = dict()
for j in lst[:]:
    if j in dictionary:
        dictionary[j] = dictionary[j]+1
    else:
        dictionary[j] = 1
# print(dictionary.items())
big_name = None
big_count = None
for keys, values in dictionary.items():
    if big_count is None or values > big_count:
        big_name = keys
        big_count = values
print(big_name, big_count)
