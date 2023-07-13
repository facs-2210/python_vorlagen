# For questions: @author Sandro
# script to demonstrate cryptography in python

import hashlib

# String to be hashed
message = "Hello, World!"

# MD5 hash
md5_hash = hashlib.md5(message.encode()).hexdigest() # Hexdigest converts the md5 object to hash string
print("MD5 Hash:", md5_hash)

# SHA-256 hash
sha256_hash = hashlib.sha256(message.encode()).hexdigest() # Hexdigest converts the md5 object to hash string
print("SHA-256 Hash:", sha256_hash)
