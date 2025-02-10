import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GIST_ID = os.getenv("GIST_ID")

CLOUDFLARED_PATH = os.getenv("CLOUDFLARED_PATH")

URL = os.getenv("URL")
