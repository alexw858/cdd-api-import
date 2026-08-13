# load configuration and hardcoded constants such as mapping template
import os
from dotenv import load_dotenv
import logging
from credential_utils import get_api_key

load_dotenv()

#Logging Configuration
LOG_FILE = "cdd_import.log"

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler(LOG_FILE), 
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# USERNAME = "tempPerson" #temporary for testing


SHARED_FOLDER = r"\\alpha\prebys_center\Chemical_Library_Screening\awooten\Users"

# API_KEY  = os.getenv("CDD_API_KEY")
API_KEY = get_api_key(USERNAME)
if API_KEY is None:
    logger.error(f"No API key found in Credential Manager for user: '{USERNAME}'")

VAULT_ID = os.getenv("CDD_VAULT_ID")
BASE_URL = f"https://app.collaborativedrug.com/api/v1/vaults/{VAULT_ID}"
HEADERS  = {"X-CDD-Token": API_KEY}



MAPPING_TEMPLATE = "AW SDF Import Test3"

#SMTP Credentials
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

USER_EMAIL = os.getenv("USER_EMAIL")