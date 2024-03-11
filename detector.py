import pandas as pd
import easyocr
from PIL import Image


class DrugDetector:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
        self.csv = pd.read_csv("data/dataset.csv")

    def detect(self, path: str) -> (str, str, list[float]):
        # downsize image first
        image = Image.open(path)
        image = image.reduce(4)
        image.save(path, optimize=True, quality=85)
        text = self.reader.readtext(path)
        return self.find_drug(text)

    def find_drug(self, result) -> (str, str, list[float]):
        for bounds, drug, confidence in result:
            words = drug.split(" ")
            for word in words:
                rows = [entry for entry in self.csv.drugName if word.lower() in entry.lower()]
                if len(rows) > 0:
                    row = self.csv[self.csv.drugName == rows[0]].iloc[0]
                    return row.drugName, row.condition, bounds
        return None
