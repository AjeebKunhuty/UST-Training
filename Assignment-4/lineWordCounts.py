lineCount, wordCount, sentenceCount = 0, 0, 0
with open("example.txt", 'r') as file:
    for line in file:
        lineCount += 1
        words = line.split()
        wordCount += len(words)
        sentenceCount += line.count('.') + line.count('!') + line.count('?')
    
print("Line Count:", lineCount)
print("Word Count:", wordCount)
print("Sentence Count:", sentenceCount)

# Output:
# Line Count: 3
# Word Count: 22
# Sentence Count: 4