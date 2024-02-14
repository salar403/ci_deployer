from os import getenv

SOURCE_IP = getenv("VALID_SOURCE_IP", None)
API_KEY = getenv("VALID_API_KEY", None)
API_KEY_HEADER = getenv("API_KEY_HEADER", "X-API-Key")
SCRIPT_PATH = getenv("SCRIPT_PATH", "./example_run.sh")
