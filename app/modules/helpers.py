import json
import requests

from pathlib import Path
from PIL import Image
from io import BytesIO

from app.modules.nasa import Nasa


def get_img(url):
    img = requests.get(url)
    return Image.open(BytesIO(img.content))


def update_apod(api_key):
    print(Path.cwd())
    img_f = Path('app/static/images/banner.jpg')
    data_path = Path('app/data/apod.json')
    nasa = Nasa(api_key)
    apod = nasa.apod()
    apod_img = get_img(apod['url'])
    apod_img.save(img_f)
    with open(data_path, 'w') as f:
        json.dump(apod, f, indent=4)
