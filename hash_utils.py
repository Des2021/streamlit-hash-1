import hashlib
import hmac
import os

def hash_text(text, algorithm='sha256'):
    """Calcula el hash de un texto plano."""
    h = hashlib.new(algorithm)
    h.update(text.encode('utf-8'))
    return h.hexdigest()

def hash_file_chunked(file, algorithm='sha256', chunk_size=8192):
    """Calcula el hash de un archivo grande en chunks."""
    h = hashlib.new(algorithm)
    for chunk in iter(lambda: file.read(chunk_size), b''):
        h.update(chunk)
    return h.hexdigest()

def with_salt(text, salt=None):
    """Agrega una sal aleatoria o dada al texto."""
    if salt is None:
        salt = os.urandom(16).hex()
    return salt, text + salt

def with_pepper(text, pepper):
    """Agrega pepper secreto (almacenado en st.secrets)."""
    return text + pepper

def hmac_text(text, key, algorithm='sha256'):
    """Calcula HMAC del texto con clave secreta."""
    return hmac.new(key.encode('utf-8'), text.encode('utf-8'), algorithm).hexdigest()

def compare_hashes(h1, h2):
    """Compara hashes de forma segura."""
    return hmac.compare_digest(h1, h2)
