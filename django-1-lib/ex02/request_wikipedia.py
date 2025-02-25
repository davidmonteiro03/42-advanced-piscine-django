#!/usr/bin/python3
import sys
import requests
import json
import dewiki


def request_wikipedia_api(lang: str, title: str) -> str:
    URL = f"https://{lang}.wikipedia.org/w/api.php"
    PARAMS = {'action': "parse",
              'page': title,
              'format': "json",
              'prop': "wikitext",
              'redirects': "true"}
    response = requests.get(url=URL, params=PARAMS)
    response.raise_for_status()
    response_json = json.loads(response.text)
    if response_json.get('error'):
        raise Exception(response_json['error']['info'])
    return dewiki.from_string(response_json['parse']['wikitext']['*'])


def main():
    argc = len(sys.argv)
    try:
        assert argc == 2, f"Usage: python3 {sys.argv[0]} <title>"
        title = ""
        for c in sys.argv[1]:
            title += '_' if c.isspace() else c
        try:
            result = request_wikipedia_api('en', title)
        except Exception:
            result = request_wikipedia_api('fr', title)
        wiki_file = f"{title}.wiki"
        with open(wiki_file, "w") as fileout:
            fileout.write(result)
            fileout.close()
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
