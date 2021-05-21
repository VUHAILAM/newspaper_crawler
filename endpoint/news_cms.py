import json
import requests

class CMS:
    def __init__(self, config=None) -> None:
        self.cms_ep = "http://10.124.68.81:8010"

    def save_post(self, data):
        url_request = f"{self.cms_ep}/v1/posts"
        response = requests.post(url_request,data=json.dumps(data), json=json.dumps(data))

        print(
            f'{url_request} status code = {response.status_code}')

        data_json = response.json()
        return data_json
