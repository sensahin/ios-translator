# iOS String Catalog Translator

This Python script helps you merge AI-generated translations into your iOS **String Catalog** (`.xcstrings`) format.  

# Setup

- python3 -m venv env
- source env/bin/activate
- pip install -r requirements.txt

## How It Works  

1. **Extract Base Template:**  
   - In **Xcode**, create a **String Catalog** (`.xcstrings`).  
   - Open the file **as source** and **copy the entire base translation**.  
   - Save it as **`base_template.json`** in this project's root directory.  

2. **Generate Translations Using AI:**  
   - Use any other **LLM (Large Language Model)**.  
   - Provide both **`base_template.json`** and **`main.py`** to the AI.  
   - Ask it to generate a **full translation JSON** for your desired language.  

3. **Save Translations:**  
   - Copy the AI-generated translation.  
   - Create a new JSON file in the **`translations/`** folder (e.g., `tr.json` for Turkish).  
   - Paste the translation inside this file.  

4. **Run the Script:**  
   ```bash
   python main.py
