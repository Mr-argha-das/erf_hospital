from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import jwt

security = HTTPBearer()
SECRET = "SECRET_KEY"

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(401, "Invalid token")