#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup


class Executor:
    def __init__(self) -> None:
        pass

    def roads_to(self, article_path: str, destination: str) -> None:
        return self.__recursive_roads_to(article_path, destination)

    def __recursive_roads_to(self, article_path: str, destination: str) -> None:
        URL = f"https://en.wikipedia.org{article_path}"
        response = requests.get(URL)
        response.raise_for_status()
        print(response.text)


def main():
    argc = len(sys.argv)
    try:
        assert argc == 2, f"Usage: python3 {sys.argv[0]} <title>"
        executor = Executor()
        executor.roads_to(f"/wiki/{sys.argv[1]}", "philosophy")
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
