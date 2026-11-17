
# Merge two files into one

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

file1.close()
file2.close()

file3 = open("codingal.txt", "w")

file3.write(content1)
file3.write("\n")
file3.write(content2)

file3.close()

print("Files merged successfully!")
