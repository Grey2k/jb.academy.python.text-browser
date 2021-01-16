import os
import requests
from collections import deque

from pages import pages


class Browser:
    COMMAND_EXIT = 'exit'
    COMMAND_BACK = 'back'

    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir
        self.history = deque()
        self.current_page = None

    def run(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        while True:
            url = input().strip()

            if url == Browser.COMMAND_EXIT:
                break

            if url == Browser.COMMAND_BACK:
                if len(self.history) == 0:
                    continue
                else:
                    url = self.history.pop()

            self.browse_page(url)

    @staticmethod
    def valid(url: str) -> bool:
        if url.find('.') == -1:
            return False

        return True

    def get_filename(self, url: str) -> str:
        if os.path.isfile(os.path.join(self.cache_dir, url)):
            return os.path.join(self.cache_dir, url)

        return os.path.join(self.cache_dir, ".".join(url.split('.')[:-1:]))

    def has_cache(self, url: str) -> bool:
        return os.path.isfile(self.get_filename(url))

    def get_from_cache(self, url: str) -> str:
        with open(self.get_filename(url)) as file:
            return ''.join([line for line in file])

    def update_cache(self, url: str, page: str) -> None:
        filename = self.get_filename(url)

        with open(f"{filename}", 'w', encoding='UTF-8') as file:
            file.write(page)

    def browse_page(self, url: str) -> None:
        real_url = url if url.startswith('https://') else 'https://' + url

        if self.has_cache(url):
            page = self.get_from_cache(url)
            print(page)

            if self.current_page is not None:
                self.history.append(self.current_page)

            self.current_page = url
            return

        if not self.valid(url):
            print('Error: Incorrect URL')
            return

        response = requests.get(real_url)

        if not response:
            print('Error: There is an Error {}'.format(response.status_code))
            return

        page = response.text

        print(page)
        self.update_cache(url, page)
        if self.current_page is not None:
            self.history.append(self.current_page)

        self.current_page = url
        return
