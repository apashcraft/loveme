import json
import requests

from pathlib import Path
from PIL import Image
from io import BytesIO

from app.modules.nasa import Nasa


def get_img(url):
    img = requests.get(url)
    return Image.open(BytesIO(img.content))
