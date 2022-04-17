import json
import requests as rq


def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")


def load_json(data):
    if not data is None:
        j = json.loads(data)
        first_name = j["results"][0]["name"]["first"]
        last_name = j["results"][0]["name"]["last"]
        return first_name, last_name


def main():
    url = "https://randomuser.me/api/"

    values = load_json(get_data(url))

    if not values is None:
        print("First Name:", values[0])
        print("Last Name:", values[1])


if __name__ == '__main__':
    main()
