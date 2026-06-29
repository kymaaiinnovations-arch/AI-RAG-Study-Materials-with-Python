# ==========================================
# Compare Stemming and Lemmatization
# ==========================================

from nltk_setup import ensure_nltk_resources

ensure_nltk_resources("wordnet", "omw-1.4")

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = [
    "running",
    "studies",
    "connected",
    "cars"
]

print("Word | Stem | Lemma")
print("-------------------------")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print(word, "|", stem, "|", lemma)
