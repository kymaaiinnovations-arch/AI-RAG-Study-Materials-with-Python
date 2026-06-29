import streamlit as st

from nltk_setup import ensure_nltk_resources

ensure_nltk_resources("punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def run_pipeline(text: str):
    """Run the NLP preprocessing pipeline on a single sentence."""
    tokens = word_tokenize(text)
    english_stopwords = set(stopwords.words("english"))

    filtered_tokens = [word for word in tokens if word.lower() not in english_stopwords]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return {
        "original_sentence": text,
        "tokens": tokens,
        "filtered_tokens": filtered_tokens,
        "lemmatized_tokens": lemmatized_tokens,
    }


st.set_page_config(
    page_title="NLP Pipeline Explorer",
    page_icon="🧠",
    layout="wide",
)

st.title("NLP Preprocessing Pipeline Explorer")
st.write(
    "Use this page to enter a test sentence and see how each NLP preprocessing step transforms the text. "
    "The pipeline includes tokenization, stopword removal, and lemmatization."
)

sentence = st.text_area(
    "Enter a test sentence:",
    value="Students are learning Artificial Intelligence quickly.",
    height=140,
)

if not sentence.strip():
    st.warning("Please enter a sentence to run the NLP pipeline.")
else:
    results = run_pipeline(sentence)

    st.markdown("## Step-by-step results")
    st.markdown("---")

    st.subheader("1. Original Sentence")
    st.write(results["original_sentence"])

    st.subheader("2. Tokenization")
    st.write("Tokenization breaks the sentence into individual words and symbols.")
    st.write(results["tokens"])
    st.dataframe({"Token": results["tokens"]})

    st.subheader("3. Stopword Removal")
    st.write(
        "Stopwords are common words like 'is', 'are', and 'the' that often do not add strong meaning to the sentence."
    )
    st.write(results["filtered_tokens"])
    st.dataframe({"Filtered Token": results["filtered_tokens"]})

    st.subheader("4. Lemmatization")
    st.write(
        "Lemmatization converts each filtered word to its dictionary base form. "
        "For example, 'learning' becomes 'learning' and 'children' becomes 'child'."
    )
    st.write(results["lemmatized_tokens"])
    st.dataframe({"Lemmatized Token": results["lemmatized_tokens"]})

    st.markdown("---")
    st.write("### Quick summary")
    st.write(
        "This pipeline demonstrates how text is transformed step-by-step: "
        "first into tokens, then cleaned by removing stopwords, and finally normalized by lemmatization."
    )
