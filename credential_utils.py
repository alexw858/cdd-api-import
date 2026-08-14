import keyring
import logging

logger = logging.getLogger(__name__)

SERVICE_NAME = "cdd_import"

def get_api_key(username):
    api_key = keyring.get_password(service_name=SERVICE_NAME, username=username)
    if api_key is None:
        logger.error(f"No stored API key found for user: '{username}'")
    return api_key

def set_api_key(username, api_key):
    keyring.set_password(service_name=SERVICE_NAME, username=username, password=api_key)
    logger.info(f"Stored API key for user: '{username}'")