# ----------------------------------------------------------------------
# Cybersecurity in Python
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# 1. Hashing and Encryption Using `hashlib`
# ----------------------------------------------------------------------
# Hashing: Hashing is a one-way operation that converts data into a fixed-size hash value.
# It's commonly used for storing passwords or verifying file integrity.
import hashlib

# a. Hashing with hashlib
def hash_password(password):
    """Hash a password using SHA-256."""
    sha256_hash = hashlib.sha256(password.encode())  # Encode and hash the password
    return sha256_hash.hexdigest()  # Return the hash as a hexadecimal string

# Example usage
password = "secure_password123"
hashed_password = hash_password(password)
print(f"Original: {password}, Hashed: {hashed_password}")

# b. Verifying a hash
def verify_password(password, hashed_password):
    """Verify a password against its hash."""
    return hash_password(password) == hashed_password

# Example usage
print(verify_password("secure_password123", hashed_password))  # Prints: True
print(verify_password("wrong_password", hashed_password))      # Prints: False

# c. Hashing Files for Integrity Checks
def hash_file(file_path):
    """Compute the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):  # Read file in chunks
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# Example usage: Save this code and test with a real file to verify integrity.

# ----------------------------------------------------------------------
# 2. Encryption and Decryption Using `cryptography`
# ----------------------------------------------------------------------
# Encryption: Encryption is a two-way operation that transforms data into a format
# that is unreadable without a key. The `cryptography` library simplifies this.

from cryptography.fernet import Fernet

# a. Generating a Key
key = Fernet.generate_key()  # Generate a random key
cipher_suite = Fernet(key)  # Create a Fernet cipher with the key
print(f"Key: {key.decode()}")  # Print the generated key

# b. Encrypting Data
message = "This is a secret message.".encode()
encrypted_message = cipher_suite.encrypt(message)  # Encrypt the message
print(f"Encrypted: {encrypted_message.decode()}")  # Print the encrypted message

# c. Decrypting Data
decrypted_message = cipher_suite.decrypt(encrypted_message).decode()  # Decrypt the message
print(f"Decrypted: {decrypted_message}")  # Prints: This is a secret message.

# ----------------------------------------------------------------------
# 3. Securing APIs and Sensitive Data
# ----------------------------------------------------------------------

# a. Secure Storage of Sensitive Data
# Do not hard-code sensitive data (e.g., API keys, passwords) in your code.
# Use environment variables or configuration files to store them securely.

import os

# Example: Storing and retrieving an API key from environment variables
# Set the environment variable before running this code
# On Linux/Mac: export API_KEY="your_api_key"
# On Windows: set API_KEY="your_api_key"
api_key = os.getenv("API_KEY")  # Retrieve the API key from environment variables
if not api_key:
    raise ValueError("API_KEY environment variable is not set!")
print(f"Retrieved API key: {api_key}")

# b. Rate-Limiting APIs
# Protect APIs from abuse using rate-limiting strategies.
# Example: Using a simple rate limiter with a dictionary (not production-grade).
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_calls, window_seconds):
        self.max_calls = max_calls
        self.window_seconds = window_seconds
        self.calls = defaultdict(list)

    def is_allowed(self, client_id):
        now = time.time()
        if client_id in self.calls:
            # Remove expired timestamps
            self.calls[client_id] = [
                timestamp for timestamp in self.calls[client_id]
                if now - timestamp < self.window_seconds
            ]
        if len(self.calls[client_id]) < self.max_calls:
            self.calls[client_id].append(now)  # Add current timestamp
            return True
        return False

# Example usage:
limiter = RateLimiter(max_calls=3, window_seconds=10)
client_id = "client_1"

for i in range(5):
    if limiter.is_allowed(client_id):
        print(f"Request {i+1} allowed.")
    else:
        print(f"Request {i+1} denied (rate limit reached).")
    time.sleep(2)

# c. Securing API Endpoints with Tokens
# Use tokens (e.g., JWT) to authenticate API requests.

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Example: Generate RSA keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Serialize keys
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Example: Sign and verify a message with RSA
message = b"Sensitive API Data"
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    print("Signature is valid!")
except Exception as e:
    print("Invalid signature:", e)

# ----------------------------------------------------------------------
# Final Thoughts and Best Practices
# ----------------------------------------------------------------------

# 1. **Hashing**:
#    - Use secure hash algorithms like SHA-256 (avoid MD5/SHA-1 as they are vulnerable).
#    - Use hashing for storing passwords (combine with salting for added security).

# 2. **Encryption**:
#    - Use modern encryption algorithms like AES (e.g., Fernet from the `cryptography` library).
#    - Never store plaintext keys in your code or configuration files.

# 3. **Securing APIs**:
#    - Store API keys and sensitive data in environment variables or secure storage.
#    - Use authentication tokens like JWT for API access.
#    - Implement rate-limiting to prevent abuse.

# These cybersecurity measures can help protect your applications and sensitive data.
