import requests


def check_success(url) -> str:
    return 'Success' if requests.get(url) else 'Fail'
