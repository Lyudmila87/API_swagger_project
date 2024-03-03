import requests


class HttpMethods:
    headers = {"Content-Type": "application/json"}

    @staticmethod
    def get(url: str) -> requests.Response:
        return requests.get(url, headers=HttpMethods.headers)

    @staticmethod
    def post(url: str, body: object) -> requests.Response:
        return requests.post(url, json=body, headers=HttpMethods.headers)

    @staticmethod
    def patch(url: str, body: object) -> requests.Response:
        return requests.patch(url, json=body, headers=HttpMethods.headers)

    @staticmethod
    def delete(url: str, body: object) -> requests.Response:
        return requests.delete(url, json=body, headers=HttpMethods.headers)
