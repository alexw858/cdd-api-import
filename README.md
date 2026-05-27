# CDD-API-Import

This project functions as an automated workflow for allowing users to upload their SDF files automatically into CDD Vault by selecting which project they want to import into.

## Files
prototype.py: a file to test basic functionality of the workflow, ensuring credentials are working and the workflow is properly configured.

## Prerequisites
Please see requirements.txt for all relevant versions of Python and packages.

## Setup steps
First, git clone the repo from Github: https://github.com/alexw858/cdd-api-import.  Create a virtual environment by running:
`python -m venv .venv`.
Then install all relevant dependencies using the requirements.txt file:
`pip install -r requirements.txt`.
Create your own .env file that lives in the same directory as the project, and use this to store important credential information such as your API key and vault ID (usually a 4 digit number).  The .env file should have 2 variables: CDD_API_KEY and CDD_VAULT_ID.

## How to run
Once everything is set up, test out the connection by running cells in order in prototype.py to ensure an active connection is there and user selection works properly.  Ensure VPN connection with the institute is active before running.

## License
This project is internal work product. Please contact Alex Wooten before reusing or redistributing.