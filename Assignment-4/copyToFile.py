targetFile = open("copy_of_example.txt", 'w')
with open("example.txt", 'r') as sourceFile:
    for line in sourceFile:
        targetFile.write(line)
targetFile.close()
print("File copied successfully to 'copy_of_example.txt'.")

# Output:
# File copied successfully to 'copy_of_example.txt'.