#!/usr/bin/env python3

import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes the password using bcrypt."""
    # Generate a random salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

if __name__ == '__main__':
    # Example usage
    password = "my_secure_password"
    hashed_password = hash_password(password)
    print(hashed_password)
