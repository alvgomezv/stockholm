from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# Generate RSA key pair
key = RSA.generate(2048)

# Get the public key for encryption
public_key = key.publickey()

# Get the private key for decryption
private_key = key

# Message to encrypt
message = b"Hello, world!"

# Create a cipher object using the public key
cipher = PKCS1_v1_5.new(public_key)

# Encrypt the message
encrypted_message = cipher.encrypt(message)

# Create a cipher object using the private key
cipher = PKCS1_v1_5.new(private_key)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message, None)

print(decrypted_message.decode())