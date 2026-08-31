import csv
import json
from pathlib import Path


class FileManager:

  def __init__(self, folder_name="data"):
    # Yeh yahan automatic check karega aur folder na hone par bana dega
    self.folder_path = Path(folder_name)
    self.folder_path.mkdir(exist_ok=True)

  def save_json(self, filename, data):
    file_path = self.folder_path / filename
    with open(file_path, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)
    print(f"[Success] JSON saved successfully at: {file_path}")

  def save_csv(self, filename, data_list):
    if not data_list:
      print("[Warning] No data available to save in CSV.")
      return
    file_path = self.folder_path / filename
    keys = data_list[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as f:
      writer = csv.DictWriter(f, fieldnames=keys)
      writer.writeheader()
      writer.writerows(data_list)
    print(f"[Success] CSV saved successfully at: {file_path}")