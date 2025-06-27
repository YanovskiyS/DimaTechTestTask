import hashlib

from src.config import settings

def calculate_signature(data: dict):
    sorted_data = sorted(str(key) for key in data.keys() if key != "signature")

    concatenated = "".join(str(data[key]) for key in sorted_data) + settings.SECRET_KEY

    return hashlib.sha256(concatenated.encode()).hexdigest()