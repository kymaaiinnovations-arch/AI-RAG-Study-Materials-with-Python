# ==========================================
# Sentence Tokenization Example
# Purpose:
# Split a paragraph into individual sentences
# ==========================================

from nltk_setup import ensure_nltk_resources

ensure_nltk_resources("punkt", "punkt_tab")

# Import sentence tokenizer
from nltk.tokenize import sent_tokenize

# Sample paragraph
paragraph = """
Artificial Intelligence is transforming industries.
It helps automate repetitive tasks.
NLP is one branch of AI.
"""

# Split paragraph into sentences
sentences = sent_tokenize(paragraph)

# Print original paragraph
print("Original Paragraph:")
print(paragraph)

# Print each sentence
print("Sentences:")

for sentence in sentences:
    print(sentence)
