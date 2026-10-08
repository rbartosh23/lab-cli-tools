from zipfile import ZipFile, BadZipFile
import zlib

with open('Ashley-Madison.txt', encoding='utf-8') as f:
    passwords = [line.strip() for line in f]

with ZipFile('whitehouse_secrets.zip') as zf:
    for i, password in enumerate(passwords):
        try:
            zf.extractall(pwd=password.encode())
        except (RuntimeError, BadZipFile, zlib.error):
            continue
        else:
            print(f"Password found: {password}")
            break