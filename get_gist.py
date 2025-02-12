import requests
import global_variables


def get_link_from_gist():
    # URL to the raw JSON file
    url = global_variables.GISTURL

    # Make a GET request to fetch the JSON
    response = requests.get(url)

    if response.status_code == 200:
        # Parse JSON content
        data = response.json()

        # Get the Cloudflare link
        cloudflare_link = data.get("cloudflare_link")

        print("Cloudflare Link:", cloudflare_link)
        return cloudflare_link
    else:
        print("Error fetching JSON:", response.text)
        return None
