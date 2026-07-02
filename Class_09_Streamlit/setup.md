# Environment Setup for Streamlit Examples

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
pip install streamlit pandas
```

## 4. Run a Streamlit app

Go to any chapter folder and run:

```bash
streamlit run app.py
```

Example:

```bash
cd "Chapter-01-Introduction"
streamlit run app.py
```

The app will open in your browser at the local Streamlit URL.
