import rsa

# RSA (Rivest-Shamir-Adleman) encryption/decryption

# Generate both the public and private keys in their respective files
def initialize_keys():
    public_key, private_key = rsa.newkeys(1024)

    with open("rsa/public.pem", "wb") as f:
        f.write(public_key.load_pkcs1("PEM"))

    with open("rsa/private.pem", "wb") as f:
        f.write(private_key.load_pkcs1("PEM"))

# Encrypt the message and write it into encrypted.message
def encrypt_message():
    with open("rsa/public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    message = "Hello"
    encrypted_message = rsa.encrypt(message.encode(), public_key)

    with open("encrypted.message", "wb") as f:
        f.write(encrypted_message)

# Decrypt the message
def decrypt_message():
    with open("rsa/private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    encrypted_message = open("rsa/encrypted.message", "rb").read()
    clear_message = rsa.decrypt(encrypted_message, private_key)
    return clear_message.decode()


if __name__ == "__main__":
    # initialize_keys()     # Initializing and encrypting have already been done, 
    # encrypt_message()     # So we won't call the functions for now
    print(decrypt_message())