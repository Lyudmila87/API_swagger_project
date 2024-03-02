import requests


class HttpMethods:
    headers = {"Content-Type": "application/json"}

    @staticmethod
    def get(url: str) -> requests.Response:
        result = requests.get(url, headers=HttpMethods.headers)
        return result

    @staticmethod
    def post(url: str, body: object) -> requests.Response:
        result = requests.post(url, json=body, headers=HttpMethods.headers)
        return result

    @staticmethod
    def patch(url: str, body: object) -> requests.Response:
        result = requests.patch(url, json=body, headers=HttpMethods.headers)
        return result

    @staticmethod
    def delete(url: str, body: object) -> requests.Response:
        result = requests.delete(url, json=body, headers=HttpMethods.headers)
        return result
