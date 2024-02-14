from os import getenv

SOURCE_IP = getenv("VALID_SOURCE_IP", None)
API_KEY = getenv("VALID_API_KEY", None)
SCRIPT_PATH = getenv("SCRIPT_PATH", "./example_run.sh")
