import os

# Define the folder structure
folders = [
    "data/raw",
    "data/processed",
    "models",
    "notebooks",
    "app/templates",
    "app/static"
]

# Define the files to be created (empty for now)
files = {
    "data/raw/iris.csv": "",
    "data/processed/iris_processed.csv": "",
    "models/iris_model.pkl": "",
    "notebooks/iris_exploration.ipynb": "",
    "app/__init__.py": "",
    "app/app.py": "",
    "app/templates/index.html": "",
    "app/static/style.css": "",
    "requirements.txt": "",
    "README.md": ""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file, content in files.items():
    with open(file, "w") as f:
        f.write(content)

print("Folder structure created successfully!")
