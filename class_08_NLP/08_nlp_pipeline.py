# ==========================================
# Complete NLP Preprocessing Pipeline
# ==========================================

from nltk_setup import ensure_nltk_resources

ensure_nltk_resources("punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4")

# Import tokenizer
from nltk.tokenize import word_tokenize

# Import stopwords
from nltk.corpus import stopwords

# Import lemmatizer
from nltk.stem import WordNetLemmatizer

# Sample sentence
sentence = "Students are learning Artificial Intelligence quickly."

# -------------------------
# Step 1: Tokenization
# -------------------------
tokens = word_tokenize(sentence)

# -------------------------
# Step 2: Stopword Removal
# -------------------------
stop_words = stopwords.words("english")

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

# -------------------------
# Step 3: Lemmatization
# -------------------------
lemmatizer = WordNetLemmatizer()

processed_words = []

for word in filtered_words:
    processed_words.append(
        lemmatizer.lemmatize(word)
    )

# -------------------------
# Display Results
# -------------------------

print("Original Sentence:")
print(sentence)

print("\nTokens:")
print(tokens)

print("\nAfter Stopword Removal:")
print(filtered_words)

print("\nAfter Lemmatization:")
print(processed_words)
