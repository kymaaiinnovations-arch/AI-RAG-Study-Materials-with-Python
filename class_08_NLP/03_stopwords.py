# ==========================================
# Stopword Removal Example
# Purpose:
# Remove common English words that usually
# don't add much meaning.
# ==========================================

from nltk_setup import ensure_nltk_resources

ensure_nltk_resources("punkt", "punkt_tab", "stopwords")

# Import tokenizer
from nltk.tokenize import word_tokenize

# Import stopword list
from nltk.corpus import stopwords

# Sample sentence
sentence = "Artificial Intelligence is changing the world."

# Convert sentence into words
words = word_tokenize(sentence)

# Load English stopwords
stop_words = stopwords.words("english")

# Empty list to store useful words
filtered_words = []

# Check every word
for word in words:
    # Convert word to lowercase before comparison
    if word.lower() not in stop_words:
        # Save useful word
        filtered_words.append(word)

# Display results
print("Original Words:")
print(words)

print("\nAfter Removing Stopwords:")
print(filtered_words)
