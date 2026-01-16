import hashlib
hash_code = "3cc6520a6890b92fb55a6b3d657fd1f6"
for i in range(999999):
    hash_bytes = str(i).encode()
    this_hash = hashlib.md5(hash_bytes).hexdigest()
    if this_hash == hash_code:
        print(i)
        break

