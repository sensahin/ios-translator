import json
import os

# Paths
BASE_TEMPLATE_PATH = "base_template.json"  # Path to your base English template
TRANSLATIONS_DIR = "translations"          # Folder with language JSON files
OUTPUT_PATH = "updated_template.json"      # Output file with merged translations

# Load the base template
with open(BASE_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    base_template = json.load(f)

# Function to merge a language file into the base template
def merge_language(base, lang_file_path):
    with open(lang_file_path, 'r', encoding='utf-8') as f:
        lang_data = json.load(f)
    
    lang_code = lang_data["sourceLanguage"]
    for key, value in lang_data["strings"].items():
        if key in base["strings"]:
            if "localizations" not in base["strings"][key]:
                base["strings"][key]["localizations"] = {}
            base["strings"][key]["localizations"][lang_code] = value["localizations"][lang_code]

# Process all language files in the translations directory
for filename in os.listdir(TRANSLATIONS_DIR):
    if filename.endswith(".json"):
        lang_file_path = os.path.join(TRANSLATIONS_DIR, filename)
        merge_language(base_template, lang_file_path)
        print(f"Merged {filename} into base template.")

# Save the updated template
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(base_template, f, ensure_ascii=False, indent=2)

print(f"Updated template saved to {OUTPUT_PATH}")