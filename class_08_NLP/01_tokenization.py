"""
==========================================
Tokenization Example
Purpose:
Break a sentence into individual words (tokens).
==========================================
"""

# Import word tokenizer
from nltk.tokenize import word_tokenize

# Sample sentence
sentence = "Artificial Intelligence is changing the world."

# Split sentence into words
tokens = word_tokenize(sentence)

# Display results
print("Original Sentence:")
print(sentence)

print("\nTokens:")
print(tokens)
