# Ransom-File-Encryptor
A small python script that encrypts all txt files in current directory and asks for ransom

---

- A small ransomware simulator. This python scripts encrypts all the txt files in directory provided. 
- It will check if secret.key exists, if it does it will load that encryption key. Otherwise generates a new encryption key using Fernet and keeps the encryption key saved as secret.key.
- I have obfuscated it to be undetectable by antivirus

---

**If someone deletes secret.key, files cannot be recovered.
If someone finds secret.key, they can decrypt everything easily.**

**TO use it more offensively, you can alter the script to send secret.key remotely. Turn it into .exe with pyinstaller and further obfuscate with tools like pyarmor or nuitka**

---

I have also uploaded the decrypting script.

**I will upload a more advanced version that encrypts all file extensions with additional functionalities soon.**


