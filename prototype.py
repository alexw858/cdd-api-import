# %% Cell 1: Load credentials and verify API connectivity
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY  = os.getenv("CDD_API_KEY")
VAULT_ID = os.getenv("CDD_VAULT_ID")
BASE_URL = f"https://app.collaborativedrug.com/api/v1/vaults/{VAULT_ID}"
HEADERS  = {"X-CDD-Token": API_KEY}

# # test basic connection first
# response = requests.get("https://app.collaborativedrug.com")
# print(response.status_code)

# Fetch available projects
response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
# print(response.status_code)
# print(response.json())

if response.status_code == 200:
    # projects = response.json().get("objects", [])
    projects = response.json()
    print(f"✓ Connected to vault {VAULT_ID}. Found {len(projects)} projects:\n")
    for i, p in enumerate(projects, 1):
        print(f"  {i}. {p['name']}  (id: {p['id']})")
else:
    print(f"✗ Connection failed: {response.status_code}")
    print(response.text)
# %%

# %% Cell 2: Project selection
# userInput = input("Please make a project selection where you would like your SDF info to be added.")
userInput = "1"

try:
    userInput = int(userInput)
    if 1 <= userInput <= len(projects):
        # selectedProject = projects[userInput+1]
        selectedProject = projects[userInput-1]
        projectName = selectedProject['name']
        projectId = selectedProject['id']

        print(f"Selected: {projectName} (id: {projectId})")
    else:
        print("problem selecting project.  Is project number in bounds for all possible options?")
except ValueError:
    print("Please enter a number for the project of interest.")



# %%
