# %% Cell 1: Load credentials and verify API connectivity
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY  = os.getenv("CDD_API_KEY")
VAULT_ID = os.getenv("CDD_VAULT_ID")
BASE_URL = f"https://app.collaborativedrug.com/api/v1/vaults/{VAULT_ID}"
HEADERS  = {"X-CDD-Token": API_KEY}

# Fetch available projects
response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)

if response.status_code == 200:
    projects = response.json().get("objects", [])
    print(f"✓ Connected to vault {VAULT_ID}. Found {len(projects)} projects:\n")
    for i, p in enumerate(projects, 1):
        print(f"  {i}. {p['name']}  (id: {p['id']})")
else:
    print(f"✗ Connection failed: {response.status_code}")
    print(response.text)