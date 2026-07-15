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


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler("cdd_import.log"), 
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)