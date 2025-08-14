from sys import exit

import requests

MENU_TEXT = """Select a number:
(1) Definition
(2) Synonyms
(3) Anytonyms
"""


def get_definition(response_content):
    print(response_content["meanings"][0]["definitions"][0]["definition"])
def main():
    print(MENU_TEXT)
    choice = input(">> ")
    if choice not in [
        "1",
        "2",
    ]:
        print("Invalid choice")
        exit(1)

    word = input("Word: ")
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        response_content = response.json()[0]

        if choice == "1":
            get_definition(response_content)

    else:
        print(f"ERROR: {response.status_code}")
        exit(1)


if __name__ == "__main__":
    main()
