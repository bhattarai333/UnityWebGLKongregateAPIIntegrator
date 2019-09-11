from pathlib import Path

data_folder = Path("Build/")
file_to_open = data_folder / "index.html"
indexHTML = file_to_open.read_text()

print(indexHTML)
