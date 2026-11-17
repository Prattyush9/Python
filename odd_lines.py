
# Remove odd-numbered lines from a file

with open("codingal.txt", "r") as file:
    lines = file.readlines()

with open("codingal.txt", "w") as file:
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            file.write(lines[i])

print("Odd-numbered lines removed successfully!")
