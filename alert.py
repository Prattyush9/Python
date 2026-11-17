
# Virus Detection Alert Program

print("Welcome to Virus Scanner")

virus = input("Enter file name to scan: ")

if virus.endswith(".exe"):
    print("WARNING! Virus Detected!")
    print("Please do not open this file.")

else:
    print("No virus detected.")
    print("File appears safe.")
