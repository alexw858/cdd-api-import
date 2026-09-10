from getpass import getpass
from credential_utils import set_api_key

def main():
    username = input("Username: ")
    api_key = getpass("CDD API key: ")
    # api_key = input("CDD API key: ")
    set_api_key(username=username, api_key=api_key)
    print(f"Stored credentials for {username}.")

if __name__ == "__main__":
    main()