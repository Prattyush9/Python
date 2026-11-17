
# Remove a specific line from a file

with open("codingal.txt", "r") as file:
    lines = file.readlines()

# Remove the second line
lines.pop(1)

with open("codingal.txt", "w") as file:
    file.writelines(lines)

print("Line removed successfully!")
