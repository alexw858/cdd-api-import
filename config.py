# load configuration and hardcoded constants such as mapping template
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY  = os.getenv("CDD_API_KEY")
VAULT_ID = os.getenv("CDD_VAULT_ID")
BASE_URL = f"https://app.collaborativedrug.com/api/v1/vaults/{VAULT_ID}"
HEADERS  = {"X-CDD-Token": API_KEY}



MAPPING_TEMPLATE = "AW SDF Import Test3"