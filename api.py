from PIL import Image, ImageDraw

from detector import DrugDetector

engine = DrugDetector()


def analyze(file_name: str) -> (str, str):
    name, condition, bounds = engine.detect(file_name)
    if name is None:
        return None, None
    image = Image.open(file_name)
    draw = ImageDraw.Draw(image)

    coords = ((float(bounds[0][0]), float(bounds[0][1])), (float(bounds[2][0]), float(bounds[2][1])))
    draw.rectangle(coords, outline=(255, 0, 0), width=7)
    image.save(file_name)
    return name, condition
