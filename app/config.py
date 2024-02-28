import json

with open("config.json","r") as inp:
    _raw_config = json.load(inp)

SOURCE_IP = _raw_config.get("VALID_SOURCE_IP")
API_KEY = _raw_config.get("VALID_API_KEY")
API_KEY_HEADER = _raw_config.get("API_KEY_HEADER")
SCRIPT_MAP = _raw_config.get("SCRIPT_MAP")


if not API_KEY_HEADER:
    raise ValueError("API_KEY_HEADER config cannot be empty!")
if not SCRIPT_MAP:
    raise ValueError("SCRIPT_MAP config cannot be empty!")
if not isinstance(SCRIPT_MAP, dict):
    raise ValueError("SCRIPT_MAP value must be a dict with mapping (endpoint: list of shellscript paths)")
for method_path in SCRIPT_MAP:
    if not isinstance(method_path, str):
        raise ValueError(f"script map method path must be a str, {method_path} is not valid")
    if not method_path.startswith("/")
        raise ValueError(f"each script map method path must start with / so {method_path} is not valid")
    if not isinstance(SCRIPT_MAP[method_path], list):
        raise ValueError(f"script map method value must be a list of shellscript paths, {SCRIPT_MAP[method_path]} is not valid")
    for script_path in SCRIPT_MAP[method_path]:
        if not isinstance(script_path, str):
            raise ValueError(f"each script path for script map methods must be str, {script_path} is not valid")
