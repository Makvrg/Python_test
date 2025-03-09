import bcrypt
import global_variables as gv


"Hash password be kept in global_variables.py"


def hash_password(password: str) -> bytes:
    # Transformation password to bytes
    password_bytes: bytes = password.encode('utf-8')
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    hashed_password: bytes = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def verify_password(input_password: str, hashed_password: bytes = gv.hash_admin_password) -> bool:
    # Transformation input password to bytes
    input_password_bytes: bytes = input_password.encode('utf-8')
    # Check password
    return bcrypt.checkpw(input_password_bytes, hashed_password)
