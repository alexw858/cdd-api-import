#main script to import chemicals

from config import *
# from sdf_utils import load_sdf, check_sdf, extract_project_name
# from cdd_client import get_projects, get_mapping_templates, validate_project, validate_template, post_slurp
# from email_utils import send_status_email
from credential_utils import get_api_key
from file_discovery import discover_user_files
from sdf_processor import process_sdf

def main():

    user_files = discover_user_files(shared_folder=SHARED_FOLDER)

    for username, sdf_files in user_files.items():
        print(username, sdf_files)
        api_key = get_api_key(username=username)
        if api_key is None:
            logger.error(f"Skipping {username}: no stored credentials found")
            continue

        for sdf in sdf_files:
            process_sdf(sdf_path=sdf, api_key=api_key, vault_id=VAULT_ID, user_email=USER_EMAIL)

    print("Completed!")


if __name__ == "__main__":
    main()