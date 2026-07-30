import bcrypt

def hash_password(password: str) -> str:
    if not isinstance(password, str) or not password.strip():
        raise ValueError("Password must be a non-empty string.")
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )
    return hashed_password.decode("utf-8")

def check_password(password: str, hashed_password: str) -> bool:
    if (
        not isinstance(password, str)
        or not isinstance(hashed_password, str)
    ):
        return False
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )