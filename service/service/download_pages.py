import wikipedia
import json


def page_to_json(page):
    try:
        return {
            "title": page,
            "content": wikipedia.page(title=page).content,
        }
    except Exception as e:
        print(e)
        return {
            "title": page,
            "content": "",
        }


if __name__ == "__main__":
    wikipedia.set_lang("en")
    pages = wikipedia.search("Tokyo sightseeing", results=6)
    json.dump(
        [
            c
            for c in [page_to_json(page) for page in pages]
            if c["content"] != ""
        ],
        open("wikipedia_pages.json", "w"))
