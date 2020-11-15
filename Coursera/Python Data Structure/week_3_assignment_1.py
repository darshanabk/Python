# Use words.txt as the file name
filename = input("Enter file name: ")
fh = open(filename)
inp = fh.read()
inp = inp.rstrip()
print(inp.upper())
