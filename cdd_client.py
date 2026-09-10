
from config import *
import requests
import json


def get_projects(api_key, vault_id):
    #dynamically populate correct credentials
    headers = {"X-CDD-Token": api_key}
    base_url = f"https://app.collaborativedrug.com/api/v1/vaults/{vault_id}"
    # Fetch available projects
    responseProjects = requests.get(f"{base_url}/projects", headers=headers, timeout=30)

    if responseProjects.status_code == 200:
        projects = responseProjects.json()
        logger.info(f"Connected to vault {vault_id}. Found {len(projects)} project(s)")
        # for i, p in enumerate(projects, 1):
        #     # print(f"{i}. {p['name']} | id: {p['id']}")
        #     # msgProjects = f"{i}. {p['name']} | id: {p['id']}"
        #     logger.info(f"{i}. {p['name']} | id: {p['id']}")
        return projects
    else:
        logger.error(f"Connection failed: {responseProjects.status_code}")
        logger.error(f"Text: {responseProjects.text}")

def get_mapping_templates(api_key, vault_id):
    #dynamically populate correct credentials
    headers = {"X-CDD-Token": api_key}
    base_url = f"https://app.collaborativedrug.com/api/v1/vaults/{vault_id}"
    responseMaps = requests.get(f"{base_url}/mapping_templates", headers=headers, timeout=30)

    if responseMaps.status_code == 200:
        mapping_templates = responseMaps.json()
        print(f"Connected to vault {vault_id}. Found {len(mapping_templates)} mapping template(s)")
        # for i, m in enumerate(mapping_templates, 1):
        #     print(f"{i}. name: {m['name']} | id: {m['id']} | owner: {m['owner']}")
        return mapping_templates
    else:
        print(f"Connection failed: {responseMaps.status_code}")
        print(responseMaps.text)

#project selection comes from sdf file, confirm it exists in vault
def validate_project(project_name, project_names):
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
            }, 
            timeout=30 #seconds
    )
    response_post.close()

    response_post.raise_for_status()

    print(response_post.status_code)
    print(f"Response post json: \n{response_post.json()}")
    return