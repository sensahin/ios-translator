# iOS String Catalog Translator

This Python script helps you merge AI-generated translations into your iOS **String Catalog** (`.xcstrings`) format.  

# Setup

```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

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



# Prompt for LLM

I am working on translating an iOS app using a **String Catalog (`.xcstrings`)**. I have a base English translation in JSON format, and I need you to generate a full translation into my desired language.

### **Instructions:**
1. **Use the provided English base template (`base_template.json`)** and translate all the strings.
2. **Preserve the JSON structure exactly** but replace English strings with the translated text.
3. **Ensure correct encoding (UTF-8) for special characters**.
4. **Maintain the `"sourceLanguage"` field and update `"localizations"`** with the target language code.
5. **Do not alter keys—only translate the values.**

### **Example of Expected Output (Simplified)**
#### **Input (`base_template.json` - English)**
```json
{
  "sourceLanguage": "en",
  "strings": {
    "welcome_message": {
      "localizations": {
        "en": "Welcome to our app!"
      }
    },
    "exit_prompt": {
      "localizations": {
        "en": "Are you sure you want to exit?"
      }
    }
  }
}
