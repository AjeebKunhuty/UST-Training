try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file was not found.")

# Output:
# Error: The file was not found.