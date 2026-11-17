
# File Handling - Count Lines in a File

file = open("codingal.txt", "r")

lines = file.readlines()

count = len(lines)

print("Total number of lines:", count)

file.close()
