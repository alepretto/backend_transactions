import time
from typing import Dict

import jwt
from local_env import config

JWT_SECRET = config.SECRET
JWT_ALGORITHM = config.ALGORITHM
print(JWT_SECRET, JWT_ALGORITHM)


def sign_jwt(user_id) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 600}

    token: str = jwt.encode(payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {"acess_token": str(token), "user": user_id}


def decode_jwt(token: str):

    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] >= time.time():
            return decoded_token
        return None

    except:
        return {}