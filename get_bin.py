import requests
import global_variables


def get_cloudflare_link():
    url = f"https://api.jsonbin.io/v3/b/{global_variables.BIN_ID}"
    headers = {
        "X-Master-Key": global_variables.API_KEY  # Required for private bins
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        link = data["record"]["cloudflare_link"]
        return link
    else:
        print("Error fetching bin:", response.text)
        return None


# Example usage
cloudflare_link = get_cloudflare_link()

if cloudflare_link:
    print("Cloudflare Link:", cloudflare_link)
else:
    print("No link found.")
