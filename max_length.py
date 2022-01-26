#

max_length = 0
max_len_line = ''
file = open("websters.txt")
for line in file:
    if(len(line) > max_length):
        max_length = len(line)
        max_len_line = line
print(max_len_line)