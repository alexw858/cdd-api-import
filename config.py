# load configuration and hardcoded constants such as mapping template
import os
from dotenv import load_dotenv
import logging

load_dotenv()

API_KEY  = os.getenv("CDD_API_KEY")
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