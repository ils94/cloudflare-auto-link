import requests
import global_variables


def publish_link_jsonbin(link):
    API_KEY = global_variables.API_KEY
    BIN_ID = global_variables.BIN_ID

    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {
        "Content-Type": "application/json",
        "X-Master-Key": API_KEY
    }

    data = {"cloudflare_link": link}
    response = requests.put(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Link published!")
    else:
        print("Error publishing:", response.text)
