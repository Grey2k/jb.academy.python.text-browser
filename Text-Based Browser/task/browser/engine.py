import os

from pages import pages


class Browser:
    COMMAND_EXIT = 'exit'

    pages = pages

    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir

    def run(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        while True:
            url = input().strip()

            if url == Browser.COMMAND_EXIT:
                break

            if self.has_cache(url):
                page = self.get_from_cache(url)
                print(page)
                continue

            if not self.valid(url):
                print('Error: Incorrect URL')
                continue

            if pages.get(url, None) is not None:
                page = pages.get(url)

                print(page)
                self.update_cache(url, page)
                continue

            print('Error: Page not Found')
            continue

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

        with open(f"{filename}", 'w') as file:
            file.write(page)
