import json
import requests


class Nasa:

    def __init__(self, api_key):
        self.api_key = api_key

    def apod(self):
        """
        Calls the NASA Astronomy Picture of the Day
        """
        url = f'https://api.nasa.gov/planetary/apod?api_key={self.api_key}'
        req = requests.get(url)
        return json.loads(req.content)
