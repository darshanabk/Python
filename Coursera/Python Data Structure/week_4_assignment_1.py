file_handle = open('romeo.txt')
reading = file_handle.read()
splitting = reading.split()
lst = list()
for line in splitting[:]:
    if line in lst[:]:
        continue
    lst.append(line)
lst.sort()
print(lst[:])
