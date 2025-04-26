import os
from cryptography.fernet import Fernet

# Config
target_dir = "./target_dir"
key_file = "secret.key"

# Load key
with open(key_file, "rb") as f:
    key = f.read()
fernet = Fernet(key)

# Decrypt function
def decrypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(file_path, "wb") as f:
        f.write(decrypted)

# Main
for filename in os.listdir(target_dir):
    if filename == "RESTORE_FILES.txt":
        continue  # <--- Skip ransom note
    if filename.endswith(".txt"):
        filepath = os.path.join(target_dir, filename)
        decrypt_file(filepath)

print("Decryption complete.")
