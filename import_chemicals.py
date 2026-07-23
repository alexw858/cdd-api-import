#main script to import chemicals

from config import *
from sdf_utils import load_sdf, check_sdf, extract_project_name
from cdd_client import get_projects, get_mapping_templates, validate_project, validate_template, post_slurp
from email_utils import send_status_email

import argparse


def main(args):
    try:
        logger.info(f"Starting import: {args.file}")
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
        logger.info(f"Import completed successfully: {args.file}")
        logger.info(f"{'='*80}")

        send_status_email(
            to_address=USER_EMAIL, 
            subject="Upload completed successfully",
            body="The upload finished without errors.", 
            attachment_path=LOG_FILE,
        )

    except Exception as e:
        logger.error(f"Upload failed: {e}")

        send_status_email(
            to_address=USER_EMAIL, 
            subject="Upload FAILED",
            body="The upload encountered an error:\n\n{e}\n\nSee attached log for details.", 
            attachment_path=LOG_FILE,
        )



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import SDF files into CDD Vault")
    parser.add_argument("--file", required=True, help="Path to SDF file, including the file name")
    args = parser.parse_args()
    main(args)