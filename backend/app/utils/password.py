import bcrypt

def hash_password(password):
    """
    Convert a plain-text password into a secure hash.
    """
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )
    return hashed_password.decode("utf-8")

def check_password(password, hashed_password):
    """
    Compare a plain-text password with a stored hash.
    """
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )