 file_handle = open('INDEX.txt')
 file_read = file_handle.read()
 striping= file_read.rstrip()
 spliting = striping.split()
 # print(spliting)
 lst = list()
 for i in range(len(spliting)):
     # print(i)
     spliting[i]=spliting[i].strip()
     if spliting[i].startswith('Name:'):
         lst.append(spliting[i+1])
         # print(lst)
     else:
         continue

 dictionary=dict()
 for j in lst[:]:
     if j in dictionary:
         dictionary[j] = dictionary[j]+1
     else:
         dictionary[j] = 1
 # print(dictionary.items())
 big_name = None
 big_count = None
 for keys,values in dictionary.items():
     if big_count == None or values > big_count:
         big_name = keys
         big_count = values
 print(big_name,big_count)

