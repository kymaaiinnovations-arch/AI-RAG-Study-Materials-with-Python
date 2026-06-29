# ==========================================
# Stemming Example
# Purpose:
# Reduce words to their root form.
# ==========================================

# Import Porter Stemmer
from nltk.stem import PorterStemmer

# Create stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "running",
    "playing",
    "studies",
    "connected",
    "walking"
]

print("Original Word -> Stemmed Word\n")

# Stem each word
for word in words:
    # Convert word into stem
    stem = stemmer.stem(word)

    print(word, "->", stem)
