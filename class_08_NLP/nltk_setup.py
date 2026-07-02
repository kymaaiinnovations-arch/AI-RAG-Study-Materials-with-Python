"""
NLTK Resource Setup
Purpose:
Download all required NLTK datasets when needed.
"""

import nltk

DEFAULT_RESOURCES = ["punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"]


def ensure_nltk_resources(*resources):
    """Download the requested NLTK resources if needed."""
    resources_to_download = resources or DEFAULT_RESOURCES

    for resource in resources_to_download:
        print(f"Downloading {resource}...")
        try:
            nltk.download(resource, quiet=True)
        except Exception as exc:
            print(f"Warning: could not download resource '{resource}': {exc}")

    return True
