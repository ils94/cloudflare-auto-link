import requests
import json
import global_variables


def publish_link_gist(link):
    GITHUB_TOKEN = global_variables.GITHUB_TOKEN
    GIST_ID = global_variables.GIST_ID

    # Gist update URL
    url = f"https://api.github.com/gists/{GIST_ID}"

    # Headers for authentication
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    json_content = json.dumps({"cloudflare_link": link}, indent=4)

    # Data to update the Gist
    data = {
        "description": "Updated Cloudflare Link",
        "files": {
            "cloudflare_link.json": {  # File name in the Gist
                "content": json_content
            }
        }
    }

    # Send a PATCH request to update the Gist
    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Link published to Gist!")
    else:
        print("Error publishing to Gist:", response.text)
