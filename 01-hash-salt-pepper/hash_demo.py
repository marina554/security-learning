import hashlib

message = "password123"

hash_value = hashlib.sha256(
    message.encode("utf-8")
).hexdigest()

print("Original:", message)
print("SHA-256:", hash_value)
print("Length:", len(hash_value))
