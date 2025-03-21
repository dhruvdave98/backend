from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Fetch credentials from .env file
BIGCOMMERCE_STORE_HASH = os.getenv("BIGCOMMERCE_STORE_HASH")
BIGCOMMERCE_ACCESS_TOKEN = os.getenv("BIGCOMMERCE_ACCESS_TOKEN")

BASE_URL = f"https://api.bigcommerce.com/stores/{BIGCOMMERCE_STORE_HASH}/v3"

# Fetch product details
@app.get("/")
def get_products():
    headers = {
        "X-Auth-Token": BIGCOMMERCE_ACCESS_TOKEN,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}/catalog/products", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch products"}
