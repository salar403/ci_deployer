from fastapi.responses import JSONResponse
from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader
from starlette.requests import Request
from fastapi import APIRouter

from app.environments import SOURCE_IP, API_KEY, SCRIPT_PATH, API_KEY_HEADER

router = APIRouter()
api_key_header = APIKeyHeader(name=API_KEY_HEADER, auto_error=False)

def validate_api_key(api_key: str = Depends(api_key_header)):
    if not API_KEY or api_key == API_KEY:
        return
    raise HTTPException(status_code=403, detail="Invalid API key")

def validate_source_ip(request: Request, authorized_ip: str = SOURCE_IP):
    client_ip = request.client.host
    if not SOURCE_IP or client_ip == authorized_ip:
        return
    raise HTTPException(status_code=403, detail="Unauthorized source IP")

@router.get("/update", dependencies=[Depends(validate_api_key), Depends(validate_source_ip)])
async def run_script():
    import subprocess
    subprocess.run(SCRIPT_PATH, shell=True)
    return JSONResponse(content={"message": "Script executed successfully"}, status_code=200)
