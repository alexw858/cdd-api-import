#main script to import chemicals

from config import *
from sdf_utils import load_sdf, check_sdf, extract_project_name
from cdd_client import get_projects, get_mapping_templates, validate_project, validate_template, post_slurp

import argparse


def main(args):
    sdf_contents = load_sdf(args.file)
    check_sdf(sdf_contents)
    project_name = extract_project_name(sdf_contents)
    # print(f"Project name from extract function: {project_name}")
    projects = get_projects()
    #extract project names from projects, a list of project dicts
    project_names = [p['name'] for p in projects]
    validate_project(project_name, project_names)
    templates = get_mapping_templates()
    print(templates)
    template_names = [t['name'] for t in templates]
    validate_template(MAPPING_TEMPLATE, template_names)
    post_slurp(args.file, project_name, MAPPING_TEMPLATE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import SDF files into CDD Vault")
    parser.add_argument("--file", required=True, help="Path to SDF file, including the file name")
    args = parser.parse_args()
    main(args)