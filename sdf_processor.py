from config import logger, LOG_FILE, MAPPING_TEMPLATE
from sdf_utils import load_sdf, check_sdf, extract_project_name
from cdd_client import get_projects, get_mapping_templates, validate_project, validate_template
from email_utils import send_status_email


def process_sdf(sdf_path, api_key, vault_id, user_email):
    try:
        logger.info(f"Starting import: {sdf_path}")
        sdf_contents = load_sdf(filename=sdf_path)
        check_sdf(sdf_contents=sdf_contents)

        #extract project name from sdf
        project_name = extract_project_name(sdf_contents=sdf_contents)
        #get projects from CDD
        projects = get_projects()
        project_names = [p['name'] for p in projects]
        #ensure project name from sdf is in project names in CDD
        validate_project(project_name=project_name, project_names=project_names)

        templates = get_mapping_templates()
        template_names = [t['name'] for t in templates]
        #ensure template in sdf exists in CDD
        validate_template(template_name=MAPPING_TEMPLATE, template_names=template_names)

        # TODO: actual CDD upload call, testing new user folder logic for now

        logger.info(f"Import completed successfully: {sdf_path}")
        send_status_email(
            to_address=user_email, 
            subject="Upload completed successfully", 
            body=f"Upload of {sdf_path} finished without errors.", 
            attachment_path=LOG_FILE
        )
    except Exception as e:
        logger.error(f"Import failed for {sdf_path}: {e}")
        send_status_email(
            to_address=user_email, 
            subject="Upload FAILED", 
            body=f"Upload of {sdf_path} failed: \n\n{e}", 
            attachment_path=LOG_FILE
        )


