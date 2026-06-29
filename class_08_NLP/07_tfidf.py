# ==========================================
# TF-IDF Example
# Purpose:
# Convert text into numerical values based
# on word importance.
# ==========================================

# Import TF-IDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "Artificial Intelligence is amazing",
    "Artificial Intelligence powers ChatGPT",
    "Python is popular"
]

# Create TF-IDF model
vectorizer = TfidfVectorizer()

# Learn vocabulary and convert documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Display vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())

# Display TF-IDF matrix
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
