#main script to import chemicals

from config import *
from sdf_utils import load_sdf, check_sdf, extract_project_name
from cdd_client import get_projects, get_mapping_templates, validate_project, validate_template, post_slurp
from email_utils import send_status_email
from file_discovery import discover_user_files
from sdf_processor import process_sdf

# import argparse


# def main(args):
def main():


    user_files = discover_user_files(shared_folder=SHARED_FOLDER)
    # print(user_files)

    for username, sdf_files in user_files.items():
        print(username, sdf_files)
        api_key = get_api_key(username=username)
        # print(api_key)
        if api_key is None:
            logger.error(f"Skipping {username}: no stored credentials found")
            continue

        for sdf in sdf_files:
            # print(sdf)
            process_sdf(sdf_path=sdf, api_key=api_key, vault_id=VAULT_ID, user_email=USER_EMAIL)

    print("Completed!")

    # try:
        # logger.info(f"Starting import: {args.file}")
        # sdf_contents = load_sdf(args.file)
        # check_sdf(sdf_contents)
        # project_name = extract_project_name(sdf_contents)
        # # print(f"Project name from extract function: {project_name}")
        # projects = get_projects()
        # #extract project names from projects, a list of project dicts
        # project_names = [p['name'] for p in projects]
        # validate_project(project_name, project_names)
        # templates = get_mapping_templates()
        # template_names = [t['name'] for t in templates]
        # validate_template(MAPPING_TEMPLATE, template_names)

        # post_slurp(args.file, project_name, MAPPING_TEMPLATE) #temp removing for now
    #     logger.info(f"Import completed successfully: {args.file}")
    #     logger.info(f"{'='*80}")

    #     send_status_email(
    #         to_address=USER_EMAIL, 
    #         subject="Upload completed successfully",
    #         body="The upload finished without errors.", 
    #         attachment_path=LOG_FILE,
    #     )

    # except Exception as e:
    #     logger.error(f"Upload failed: {e}")

    #     send_status_email(
    #         to_address=USER_EMAIL, 
    #         subject="Upload FAILED",
    #         body="The upload encountered an error:\n\n{e}\n\nSee attached log for details.", 
    #         attachment_path=LOG_FILE,
    #     )

        #all commented code above now handled by process_sdf() function





if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Import SDF files into CDD Vault")
    # parser.add_argument("--file", required=True, help="Path to SDF file, including the file name")
    # args = parser.parse_args()
    # main(args)
    main()