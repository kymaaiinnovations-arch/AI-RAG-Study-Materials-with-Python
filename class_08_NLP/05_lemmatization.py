# ==========================================
# Lemmatization Example
# Purpose:
# Convert words into their dictionary form.
# ==========================================

from nltk_setup import ensure_nltk_resources

ensure_nltk_resources("wordnet", "omw-1.4")

# Import WordNet Lemmatizer
from nltk.stem import WordNetLemmatizer

# Create lemmatizer object
lemmatizer = WordNetLemmatizer()

# List of words
words = [
    "studies",
    "cars",
    "children"
]

print("Original Word -> Lemma\n")

# Convert each word into its lemma
for word in words:
    lemma = lemmatizer.lemmatize(word)

    print(word, "->", lemma)
