import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
API_KEY = os.getenv("API_KEY")
BIN_ID = os.getenv("BIN_ID")
