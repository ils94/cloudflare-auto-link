import requests
import json
import global_variables


def get_link_from_gist():
    GITHUB_TOKEN = global_variables.GITHUB_TOKEN
    GIST_ID = global_variables.GIST_ID

    # Gist API URL
    url = f"https://api.github.com/gists/{GIST_ID}"

    # Headers with authentication
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Make a GET request to fetch the Gist
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        gist_data = response.json()

        # Extract the file content (assuming "cloudflare_link.json" is the filename)
        file_content = gist_data["files"]["cloudflare_link.json"]["content"]

        # Parse JSON content
        data = json.loads(file_content)

        # Get the Cloudflare link
        cloudflare_link = data.get("cloudflare_link")

        print("Cloudflare Link:", cloudflare_link)
        return cloudflare_link
    else:
        print("Error fetching Gist:", response.text)
        return None


link = get_link_from_gist()
