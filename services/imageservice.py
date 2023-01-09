import requests
from dotenv import load_dotenv
import os
load_dotenv()


class ImageService:
    def __init__(self):
        self.base_url = 'https://bing-image-search1.p.rapidapi.com/images/search'

    def get_img(self, query: str) -> str:
        querystring = {"q": query}
        headers = {
            "X-RapidAPI-Key": os.environ["X-RapidAPI-Key"],
            "X-RapidAPI-Host": os.environ["X-RapidAPI-Host"]
        }
        data = requests.get(self.base_url, headers=headers, params=querystring)
        return data.json()['value'][6]['contentUrl']


if __name__ == '__main__':
    img = ImageService()
    url_img = img.get_img('Ribeirão Preto')
    print(url_img)
