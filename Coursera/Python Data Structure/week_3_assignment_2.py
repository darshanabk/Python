filename = input("Enter file name: ")
file_handle = open(filename)
count = 0
addition = 0.0
for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    addition = addition+float(line[20:])
print("Average spam confidence:",addition/count)
