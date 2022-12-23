import requests


class ImageService:
    def __init__(self):
        self.base_url = 'https://bing-image-search1.p.rapidapi.com/images/search'

    def get_img(self, query: str) -> str:
        querystring = {"q": query}
        headers = {
            "X-RapidAPI-Key": "d4561e0951mshd9cc138de72db3dp18bf4ejsn26b4c39fccaf",
            "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
        }
        data = requests.get(self.base_url, headers=headers, params=querystring)
        return data.json()['value'][6]['contentUrl']


if __name__ == '__main__':
    img = ImageService()
    req = img.get_img('Ribeirão Preto')
    print(req)
