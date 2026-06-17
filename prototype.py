# %% Cell 1: Load credentials and verify API connectivity
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY  = os.getenv("CDD_API_KEY")
VAULT_ID = os.getenv("CDD_VAULT_ID")
BASE_URL = f"https://app.collaborativedrug.com/api/v1/vaults/{VAULT_ID}"
HEADERS  = {"X-CDD-Token": API_KEY}

# # test basic connection first
# response = requests.get("https://app.collaborativedrug.com")
# print(response.status_code)

# Fetch available projects
responseProjects = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
print(f"{BASE_URL}/projects")
print(responseProjects.status_code)
print(responseProjects.json())

if responseProjects.status_code == 200:
    # projects = response.json().get("objects", [])
    projects = responseProjects.json()
    print(f"✓ Connected to vault {VAULT_ID}. Found {len(projects)} project(s):\n")
    for i, p in enumerate(projects, 1):
        print(f"  {i}. {p['name']}  (id: {p['id']})")
else:
    print(f"✗ Connection failed: {responseProjects.status_code}")
    print(responseProjects.text)


responseMaps = requests.get(f"{BASE_URL}/mapping_templates", headers=HEADERS)
print(responseMaps.status_code)
print(responseMaps.json())
# %%

# # %% Cell 2: Project selection (user selects; OLD method)
# # userInput = input("Please make a project selection where you would like your SDF info to be added.")
# userInput = "1"

# try:
#     userInput = int(userInput)
#     if 1 <= userInput <= len(projects):
#         # selectedProject = projects[userInput+1]
#         selectedProject = projects[userInput-1]
#         projectName = selectedProject['name']
#         projectId = selectedProject['id']

#         print(f"Selected: {projectName} (id: {projectId})")
#     else:
#         print("problem selecting project.  Is project number in bounds for all possible options?")
# except ValueError:
#     print("Please enter a number for the project of interest.")
# # %%


# %% Cell 3: Load SDF file, grab project name from SDF, select mapping template ("parser type", POST to Slurps endpoint)
# --- CONFIG ---
# SDFFileName = "data/Test compounds_projectName.sdf"
SDFFileName = "data/Test compounds_RR_projectName.sdf"
# --------------
with open(SDFFileName, "r") as f:
    # sdf_contents = f.read()
    sdf_contents = f.read().splitlines()

# print(type(sdf_contents))
# print(len(sdf_contents))
# print(sdf_contents)

# print(repr(sdf_contents[114:118]))

projectNames = []

for i, line in enumerate(sdf_contents):
    if line.strip() == ">  <Project name>":
        # projectName = line[i+1]
        projectName = sdf_contents[i+1]
        projectNames.append(projectName)
        # print(projectName)

# print(projectNames)

if len(set(projectNames)) == 1:
    projectName = projectNames[0]
    print(f"Project name found: {projectName}")
else:
    raise Exception(f"Mixed project names found in SDF file: {set(projectNames)}")



# mappingTemplate = "AW SDF Import Test1"
mappingTemplate = "AW SDF Import Test3"

# responseMaps.
mapTemplates = []
for mapTemp in responseMaps.json():
    # print(mapTemp['name'])
    mapTemplates.append(mapTemp['name'])
# print(mapTemplates)

if mappingTemplate not in mapTemplates:
    raise Exception(f"Mapping template {mappingTemplate} not found in vault.  Available templates: {mapTemplates}")
else:
    print(f"Mapping template found: {mappingTemplate}")


# %%


# %%
#test code
# print(sdf_contents[50:80])
# for line in sdf_contents[100:150]:
#     print(line)

# print(responseMaps.json()[0].keys())
# print(responseMaps.json()[1]['name'])


payload = {
    "project": projectName, 
    "mapping_template": mappingTemplate, 
    "autoreject": "true"
}


# # postDestination = requests.post(f"{BASE_URL}/slurps", headers=HEADERS)

with open(SDFFileName, "rb") as sdf_file:
    response_post = requests.post(
        f"{BASE_URL}/slurps", 
        headers=HEADERS, 
        files={
            "file": sdf_file, 
            "json": (None, json.dumps(payload), "application/json")
        }
    )
response_post.close()

print(response_post.status_code)
print(response_post.json())

# %%


# %%

# print(response_post.status_code)
# print(response_post.json())
# %%