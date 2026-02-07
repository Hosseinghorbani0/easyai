import os

target_dir = "docs"
print(f"Updating documentation in {target_dir}...")

for filename in os.listdir(target_dir):
    if filename.endswith(".md"):
        path = os.path.join(target_dir, filename)
        print(f"Processing {filename}...")
        
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. Update Code Imports (Must be snake_case)
        new_content = content.replace("from easyai import", "from ask_ai import")
        new_content = new_content.replace("import easyai", "import ask_ai")
        # 2. Update Text/Pip (Kebab-case preferred for branding/pip)
        new_content = new_content.replace("easyai", "ask-ai")
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

print("Documentation update complete.")
