import hvac, time

class Vault:

    def __init__(self, url: str):
        self.url = url
        self._client = None

        self.__init__client()

    def __init__client(self):
        self._client = hvac.Client(url=self.url)

    @property
    def client(self):
        return self._client

    def unseal(self, unseal_keys: list):

        CHECK_ATTEMPT_LIMIT = 3
        check_attempts = 0

        if not self.client.sys.is_sealed():
            print('Vault is unsealed.')
        else:
            print('Unsealing vault...')
            try:
                self.client.sys.submit_unseal_keys(keys=unseal_keys)
            except:
                pass
            while check_attempts < CHECK_ATTEMPT_LIMIT:
                time.sleep(5)
                if not self.client.sys.is_sealed():
                    check_attempts = CHECK_ATTEMPT_LIMIT
                    print('Vault successfully unsealed.')
                else:
                    check_attempts = check_attempts + 1

