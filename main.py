import requests


def get_request(user_url: str):
    url = user_url
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    print(get_request("http://localhost:63342/website_layout(HW)/contacts.html"))
