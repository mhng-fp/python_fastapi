# app/shortener.py

# Base properties
domain = "http://localhost:8080/"
allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
base = len(allowed_characters)

# Simulated Database Storage
id_to_url_map = {}
url_to_id_map = {}
current_id = 100000

def encode_base62(id_val: int) -> str:
    """Converts a unique Base10 database ID into a Base62 alphanumeric string token."""
    num = id_val
    sb = []
    while num > 0:
        sb.append(allowed_characters[num % base])
        num //= base
    sb.reverse()
    return "".join(sb)

def decode_base62(str_val: str) -> int:
    """Decodes a Base62 string token back into its source database numeric ID."""
    num = 0
    for char in str_val:
        num = num * base + allowed_characters.index(char)
    return num

def shorten(long_url_str: str) -> str:
    """Shortens a given long URL string and stores it in the data maps."""
    global current_id

    # Return existing shortened token if URL was already processed
    if long_url_str in url_to_id_map:
        existing_id = url_to_id_map[long_url_str]
        return domain + encode_base62(existing_id)

    # Save entry and increment the counter
    id_val = current_id
    current_id += 1

    id_to_url_map[id_val] = long_url_str
    url_to_id_map[long_url_str] = id_val

    return domain + encode_base62(id_val)

def resolve(short_code: str) -> str:
    """Resolves a shortened URL code back to its original form."""
    id_val = decode_base62(short_code)
    return id_to_url_map.get(id_val)
