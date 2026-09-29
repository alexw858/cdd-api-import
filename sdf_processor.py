from config import logger, LOG_FILE, MAPPING_TEMPLATE
from sdf_utils import load_sdf, check_sdf, extract_project_name
# from cdd_client import get_projects, get_mapping_templates, validate_project, validate_template, post_slurp
from cdd_client import get_projects, get_mapping_templates, build_project_maps, resolve_project, validate_template, post_slurp
from email_utils import send_status_email
import requests


def process_sdf(sdf_path, api_key, vault_id, user_email):
    try:
        logger.info(f"Starting import: {sdf_path}")
        sdf_contents = load_sdf(filename=sdf_path)
        check_sdf(sdf_contents=sdf_contents)

        #extract project name from sdf
        # project_name = extract_project_name(sdf_contents=sdf_contents)
        sdf_project = extract_project_name(sdf_contents=sdf_contents)
        #get projects from CDD
        projects = get_projects(api_key=api_key, vault_id=vault_id)
        project_names = [p['name'] for p in projects]
        # #ensure project name from sdf is in project names in CDD
        # validate_project(project_name=project_name, project_names=project_names)

        project_names, project_code_map = build_project_maps(projects=projects)
        resolved_project = resolve_project(sdf_project=sdf_project, project_names=project_names, project_code_map=project_code_map)

        templates = get_mapping_templates(api_key=api_key, vault_id=vault_id)
        template_names = [t['name'] for t in templates]
        #ensure template in sdf exists in CDD
        validate_template(template_name=MAPPING_TEMPLATE, template_names=template_names)

        #upload data to CDD
        # post_slurp(sdf_filepath=sdf_path, project_name=project_name, template_name=MAPPING_TEMPLATE, api_key=api_key, vault_id=vault_id)
        post_slurp(sdf_filepath=sdf_path, project_name=resolve_project, template_name=MAPPING_TEMPLATE, api_key=api_key, vault_id=vault_id)
        logger.info(f"Import completed successfully: {sdf_path}")

        send_status_email(
            to_address=user_email, 
            subject="Upload completed successfully", 
            body=f"Upload of {sdf_path} finished without errors.", 
            attachment_path=LOG_FILE
        )
    except requests.exceptions.Timeout as e:
        logger.error(f"Request to CDD timed out for {sdf_path}: {e}")
        send_status_email(
            to_address=user_email, 
            subject="Upload FAILED - Timeout", 
            body=f"Upload of {sdf_path} timed out while contacting CDD.  This may be a temporary network issue - it's suggested to try again later. \n\n{e}", 
            attachment_path=LOG_FILE
        )
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Request to CDD had a connection error for {sdf_path}: {e}")
        send_status_email(
            to_address=user_email, 
            subject="Upload FAILED - Connection Error", 
            body=f"Upload of {sdf_path} failed due to a connection error while contacting CDD.  This may be a temporary network issue - it's suggested to try again later. \n\n{e}", 
            attachment_path=LOG_FILE
        )
    
    except Exception as e:
        error_detail = ""
        if hasattr(e, "response") and e.response is not None:
            try:
                error_detail = e.response.json()
            except ValueError:
                error_detail = e.response.text
            print(error_detail)

        logger.error(f"Import failed for {sdf_path}: {e}\nDetails: {error_detail}")
        send_status_email(
            to_address=user_email, 
            subject="Upload FAILED", 
            body=f"Upload of {sdf_path} failed: \n\n{e}\n\nDetails: {error_detail}", 
            attachment_path=LOG_FILE
        )