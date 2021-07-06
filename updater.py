import logging
import os
import subprocess
import shlex
from dotenv import load_dotenv

load_dotenv('config.env')

logging.basicConfig(format='Updating Bot - %(levelname)s - %(message)s',level=logging.INFO)

LOGGER = logging.getLogger(__name__)

def run_update(args, *, output=False, shell=False, cd=None):
    if not shell:
        if output:
            proc = subprocess.Popen(
                shlex.split(args), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cd
            )
            while True:
                output = proc.stdout.readline()
                if output == b"" and proc.poll() is not None:
                    return
                if output:
                    print(output.decode("utf-8").strip())
        return subprocess.run(shlex.split(args), cwd=cd).returncode
    else:
        if output:
            return (
                subprocess.run(
                    args,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cd,
                )
                .stdout.decode("utf-8")
                .strip()
            )
        return subprocess.run(args, shell=True, cwd=cd).returncode


def getConfig(name: str):
    return os.environ[name]

try:
    USE_SERVICE_ACCOUNTS = getConfig('USE_SERVICE_ACCOUNTS')
    if USE_SERVICE_ACCOUNTS.lower() == 'true':
        USE_SERVICE_ACCOUNTS = True        
    else:
        raise KeyError
except KeyError:
    USE_SERVICE_ACCOUNTS = False


try:
    TOKEN_SA_PICKLE_URL = getConfig('TOKEN_SA_PICKLE_URL')
    if len(TOKEN_SA_PICKLE_URL) == 0:
        raise KeyError
except KeyError:
    TOKEN_SA_PICKLE_URL = None
    
try:
    ACCOUNTS_ZIP_URL = getConfig('ACCOUNTS_ZIP_URL')
    if len(ACCOUNTS_ZIP_URL) == 0:
        raise KeyError
except KeyError:        
    ACCOUNTS_ZIP_URL = None

try:
    CREDENTIAL_JSON = getConfig('CREDENTIAL_JSON')
    if len(CREDENTIAL_JSON) == 0:
        raise KeyError
except KeyError:
    CREDENTIAL_JSON = None
    
try:
    CONFIG_ENV = getConfig('CONFIG_ENV')
    if len(CONFIG_ENV) == 0:
        raise KeyError
except KeyError:
    CONFIG_ENV = None

try:
    TOKEN_PICKLE_URL = getConfig('TOKEN_PICKLE_URL')
    if len(TOKEN_PICKLE_URL) == 0:
        raise KeyError
except KeyError:
    TOKEN_PICKLE_URL = None


def WithServiceAccount():
    if ACCOUNTS_ZIP_URL is not None:
        LOGGER.info(f"Downdloading accounts.zip from {ACCOUNTS_ZIP_URL}")
        run_update(f"wget -q {ACCOUNTS_ZIP_URL} -O ./accounts.zip")
        run_update("unzip -o -q accounts.zip -d ./accounts")
        run_update("rm accounts.zip")
        LOGGER.info("unzip accounts.zip is Done!")
    else:
        LOGGER.warning("ACCOUNTS_ZIP_URL Is not found")
    if TOKEN_SA_PICKLE_URL is not None:
        LOGGER.info(f"Downdloading token_sa.pickle from {TOKEN_SA_PICKLE_URL}")
        run_update(f"wget -q {TOKEN_SA_PICKLE_URL} -O ./token_sa.pickle")
        LOGGER.info("TOKEN_SA_PICKLE is Save!")
    else:
        LOGGER.warning("TOKEN_SA_PICKLE_URL Is not found")
    if CONFIG_ENV is not None:
        LOGGER.info(f"Downdloading config.env from {CONFIG_ENV}")
        run_update(f"wget -q {CONFIG_ENV} -O ./config.env")
        LOGGER.info("config.env is Save!")
    else:
        LOGGER.warning("CONFIG_ENV is Not Found")


def WithoutServiceAccount():
    LOGGER.warning("You are not using service account")
    if TOKEN_PICKLE_URL is not None:
        LOGGER.info(f"Downdloading token.pickle from {TOKEN_PICKLE_URL}")
        run_update(f"wget -q {TOKEN_PICKLE_URL} -O ./token.pickle")
        LOGGER.info("token.pickle is Save!")
    else:
        LOGGER.warning("TOKEN_PICKLE_URL is not found!")
    if CREDENTIAL_JSON is not None:
        LOGGER.info(f"Downdloading credentials.json from {CREDENTIAL_JSON}")
        run_update(f"wget -q {CREDENTIAL_JSON} -O ./credentials.json")
        LOGGER.info("credentials.json is Save!")
    else:
        LOGGER.warning("CREDENTIAL_JSON is Not Found")
    if CONFIG_ENV is not None:
        LOGGER.info(f"Downdloading config.env from {CONFIG_ENV}")
        run_update(f"wget -q {CONFIG_ENV} -O ./config.env")
        LOGGER.info("config.env is Save!")
    else:
        LOGGER.warning("CONFIG_ENV is Not Found")


if USE_SERVICE_ACCOUNTS:
    WithServiceAccount()
else:
    WithoutServiceAccount()