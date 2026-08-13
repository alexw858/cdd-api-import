
from config import *
import requests
import json


def get_projects(api_key, vault_id):
    #dynamically populate correct credentials
    headers = {"X-CDD-Token": api_key}
    base_url = f"https://app.collaborativedrug.com/api/v1/vaults/{vault_id}"
    # Fetch available projects
#     responseProjects = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
    responseProjects = requests.get(f"{base_url}/projects", headers=headers)
    # print(f"{BASE_URL}/projects")
    # print(responseProjects.status_code)
    # print(responseProjects.json())

    if responseProjects.status_code == 200:
        # projects = response.json().get("objects", [])
        projects = responseProjects.json()
        # print(f"Connected to vault {VAULT_ID}. Found {len(projects)} project(s):\n")
        # logger.info(f"Connected to vault {VAULT_ID}. Found {len(projects)} project(s):")
        logger.info(f"Connected to vault {vault_id}. Found {len(projects)} project(s):")
        # for i, p in enumerate(projects, 1):
        #     # print(f"{i}. {p['name']} | id: {p['id']}")
        #     # msgProjects = f"{i}. {p['name']} | id: {p['id']}"
        #     logger.info(f"{i}. {p['name']} | id: {p['id']}")
        return projects
    else:
        # print(f"Connection failed: {responseProjects.status_code}")
        logger.error(f"Connection failed: {responseProjects.status_code}")
        # print(responseProjects.text)
        logger.error(f"Text: {responseProjects.text}")

def get_mapping_templates(api_key, vault_id):
    #dynamically populate correct credentials
    headers = {"X-CDD-Token": api_key}
    base_url = f"https://app.collaborativedrug.com/api/v1/vaults/{vault_id}"
    # responseMaps = requests.get(f"{BASE_URL}/mapping_templates", headers=HEADERS)
    responseMaps = requests.get(f"{base_url}/mapping_templates", headers=headers)
    print(responseMaps.status_code)
    print(responseMaps.json())

    if responseMaps.status_code == 200:
        # projects = response.json().get("objects", [])
        mapping_templates = responseMaps.json()
        # print(f"Connected to vault {VAULT_ID}. Found {len(mapping_templates)} mapping template(s):\n")
        print(f"Connected to vault {vault_id}. Found {len(mapping_templates)} mapping template(s):\n")
        # for i, m in enumerate(mapping_templates, 1):
        #     print(f"{i}. name: {m['name']} | id: {m['id']} | owner: {m['owner']}")
        return mapping_templates
    else:
        print(f"Connection failed: {responseMaps.status_code}")
        print(responseMaps.text)

#project selection comes from sdf file, confirm it exists in vault
def validate_project(project_name, project_names):
    # print(f"Project name coming into validate function: {project_name}")
    # print(f"project_names coming into validate function: {project_names}")
    if project_name in project_names:
        print(f"Found project '{project_name}' in list of project names successfully.")
        return
    else:
        raise Exception(f"Project name mismatch.  Unable to find project {project_name} in full list of project_names: {project_names}.")

#template is hard-coded in config.py, just confirm it exists currently in vault
def validate_template(template_name, template_names):
    if template_name in template_names:
        print(f"Found template '{template_name}' in list of templates successfully.")
        return
    else:
        raise Exception(f"Template name mismatch.  Unable to find template {template_name} in full list of mapping templates: {template_names}.")
    

def post_slurp(sdf_filepath, project_name, template_name, api_key, vault_id):

    base_url = f"https://app.collaborativedrug.com/api/v1/vaults/{vault_id}"
    headers = {"X-CDD-Token": api_key}

    payload = {
    "project": project_name, 
    "mapping_template": template_name, 
    "autoreject": "true"
    }

    with open(sdf_filepath, "rb") as sdf_file:
        response_post = requests.post(
            f"{base_url}/slurps", 
            headers=headers, 
            files={
                "file": sdf_file, 
                "json": (None, json.dumps(payload), "application/json")
            }
    )
    response_post.close()

    print(response_post.status_code)
    print(response_post.json())
    return