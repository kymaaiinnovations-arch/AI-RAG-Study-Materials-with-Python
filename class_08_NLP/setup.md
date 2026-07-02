# Environment Setup for NLP Examples

## 1. Create a virtual environment

```bash
python3 -m venv .venv
```

## 2. Activate the virtual environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Install required packages

```bash
pip install -r requirements.txt
```

If you want to install them manually:

```bash
pip install nltk scikit-learn
```

## 4. Run the first NLP example

```bash
python 001_first_step_nltk_setup.py
```

## 5. Optional: download NLTK data

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```
