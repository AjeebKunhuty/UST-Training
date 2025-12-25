word = input("Enter the word to search: ")
found = False
with open("example.txt", 'r') as file:
    for lineNumber, line in enumerate(file, start=1):
        if word in line:
            print(f"Word '{word}' found in line {lineNumber}: {line.strip()}")
            found = True
if not found:
    print(f"Word '{word}' not found in the file.")

# Output 1:
# Enter the word to search: UST
# Word 'UST' found in line 1: Hello, UST!

# Output 2:
# Enter the word to search: ust
# Word 'ust' not found in the file.