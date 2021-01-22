import time, base64, json, os
from vaultunseal.vault import Vault

def get_config():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/config.json'))
    with open(config_path) as file:
        config_data = json.load(file)
    return config_data

def main():

    config = get_config()
    while True:
        vault = Vault(url=config.get('url'))
        unseal_keys = config.get('keys')
        vault.unseal(unseal_keys=unseal_keys)
        vault = None
        time.sleep(60)
        