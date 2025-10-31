import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security


bearer = HTTPBearer()

load_dotenv()

secret_key = os.getenv("secret_key")

def  create_token(details: dict, expiry: int):
    expire = datetime.now() + timedelta(minutes=expiry)
    
    details.update({"exp": expire})
    
    encoded_jwt = jwt.encode(details, secret_key)
    
    return encoded_jwt

def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):
    # Another way to go about the code below:
    
    # payload = Request.headers.get("Authorization")
    
    # "Authorization": "Bearer jhfqhkfnknvnbjnkjkn"
    
    # payload = "Bearer jhfqhkfnknvnbjnkjkn"
    
    # token = payload.split(" ")[1]
    
    token = request.credentials
    
    verified_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    
    # expiry_time = verified_token.get("exp")
    
    return {
        "id": verified_token.get("id"),
        "email": verified_token.get("email"),
        "userType": verified_token.get("userType")
    }