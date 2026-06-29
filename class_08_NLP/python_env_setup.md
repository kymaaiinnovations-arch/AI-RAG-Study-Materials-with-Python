# Python Environment Setup for NLP Examples

## 1. Create a virtual environment

```bash
python -m venv .venv
```

## 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Install required packages

```bash
pip install nltk scikit-learn
```

## 4. run filr 001_first_step_nltk_setup.py

```bash
python 001_first_step_nltk_setup.py
```

<!-- ## 4. Download NLTK data

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
``` -->

## 5. Run an example

```bash
python tokenization.py
```
