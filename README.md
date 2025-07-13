# HW 04

## Setup (with virtual environment)

1. **Create a virtual environment** (recommended to isolate dependencies):

```bash
python -m venv venv
```

2. **Activate the virtual environment**:

- On Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

- On Windows (cmd):

```cmd
.\venv\Scripts\activate.bat
```

- On Linux/macOS:

```bash
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the assistant bot**:

```bash
python 4_assistant_bot.py
```


## Creating `requirements.txt`

To create a `requirements.txt` file with your current dependencies, run:

```bash
pip freeze > requirements.txt
```

This will save all installed packages in your virtual environment to the file.

---
