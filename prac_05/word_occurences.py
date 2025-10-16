"""
Word Occurrence Counter
Estimate Time: 15 minutes
Actual Time: 19 minutes
"""

text = "how much wood would a wood chuck chuck if a woodchuck could chuck wood"
words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

max_length = max(len(word) for word in word_counts)

for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")
