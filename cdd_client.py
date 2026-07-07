
def get_projects():
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


def get_mapping_templates():
    responseMaps = requests.get(f"{BASE_URL}/mapping_templates", headers=HEADERS)
    print(responseMaps.status_code)
    print(responseMaps.json())

#project selection comes from sdf file, confirm it exists in vault
def validate_project(project_name, projects):
    if project_name in projects:
        print(f"Found project {project_name} in list of projects successfully.")
        return
    else:
        raise Exception(f"Project name mismatch.  Unable to find project {project_name} in full list of projects: {projects}.")

#template is hard-coded in config.py, just confirm it exists currently in vault
def validate_template(template_name, templates):
    if template_name in templates:
        print(f"Found project {template_name} in list of templates successfully.")
        return
    else:
        raise Exception(f"Template name mismatch.  Unable to find template {template_name} in full list of mapping templates: {templates}.")
    

def post_slurps(sdf_file, project_name, template_name):
    return