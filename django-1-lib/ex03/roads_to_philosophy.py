#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup, _typing


class roads_to_philosophy:
    def __init__(self) -> None:
        self.__visited = []

    def execute(self,
                article_path: str) -> None:
        return self.__recursive_execute(article_path)

    def __recursive_execute(self,
                            article_path: str) -> None:
        __URL = f"https://en.wikipedia.org{article_path}"

        try:
            __response = requests.get(__URL)
            __response.raise_for_status()
        except Exception:
            raise Exception("It's a dead end !")

        __soup = BeautifulSoup(__response.text, 'html.parser')
        __tables = __soup.find_all('table')
        [__t.extract() for __t in __tables]

        __title = __soup.find(id="firstHeading").text
        if __title in self.__visited:
            raise Exception("It leads to an infinite loop !")
        self.__visited.append(__title)
        print(__title)

        if __title == "Philosophy":
            __number_of_roads = len(self.__visited)
            __starting_point = self.__visited[0]
            __destination = str(self.__visited[-1]).lower()
            return print(f"\
{__number_of_roads} roads from {__starting_point} to {__destination} !")

        __content = __soup.find(id="mw-content-text")

        __links = self.__extract_links(__content, 'p') + \
            self.__extract_links(__content, 'li')
        for __l in __links:
            __href = __l.attrs.get('href')
            if not __href or not __href.startswith('/wiki/') or \
               __href.startswith('/wiki/Help'):
                continue
            return self.__recursive_execute(__href)

        raise Exception("It leads to a dead end !")

    def __extract_links(self,
                        content: _typing._AtMostOneElement,
                        tag: str) -> _typing._QueryResults:
        __result: _typing._QueryResults = []
        __elems: _typing._QueryResults = content.find_all(tag)
        __parent_depth = 0
        for __elem in __elems:
            for __ in __elem.contents:
                if __parent_depth == 0:
                    __tmp_soup = BeautifulSoup(str(__), 'html.parser')
                    __links = __tmp_soup.find_all('a')
                    for __l in __links:
                        __result.append(__l)
                __parsed = str(__.text)
                __parent_depth += __parsed.count('(')
                __parent_depth -= __parsed.count(')')
        return __result


def main():
    argc = len(sys.argv)
    try:
        assert argc == 2, f"Usage: python3 {sys.argv[0]} <title>"
        roads = roads_to_philosophy()
        roads.execute(f"/wiki/{sys.argv[1].strip()}")
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
