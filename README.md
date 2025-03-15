# iOS String Catalog Translator

This Python script helps you merge AI-generated translations into your iOS **String Catalog** (`.xcstrings`) format.  

# Setup

```bash
    python3 -m venv env
    source env/bin/activate

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
```
# Prompt for LLM

I am working on translating an iOS app using a **String Catalog (`.xcstrings`)**. I have a base English translation in JSON format, and I need you to generate a full translation into my desired language.

### **Instructions:**

1. **Keep the JSON structure identical** to the example.
2. **Only translate the `"value"` field** inside `"stringUnit"`.
3. **Preserve placeholders like `%@`, `%lld`, etc.**, as they are dynamic content in iOS.
4. **Ensure UTF-8 encoding** for special characters.
5. **Maintain `"state": "translated"` for all entries**.
6. **Use the correct language code in `"sourceLanguage"`**.

---

### **Example of Expected Output**
#### **Input (`base_template.json` - English)**
```json
{
    "sourceLanguage": "en",
    "strings": {
        "welcome_message": {
            "localizations": {
                "en": {
                    "stringUnit": {
                        "state": "translated",
                        "value": "Welcome to our app!"
                    }
                }
            }
        },
        "%lld days ago": {
            "localizations": {
                "en": {
                    "stringUnit": {
                        "state": "translated",
                        "value": "%lld days ago"
                    }
                }
            }
        }
    }
}