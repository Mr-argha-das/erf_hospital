import uuid, os

def save_file(file, folder):
    os.makedirs(f"uploads/{folder}", exist_ok=True)
    name = f"{uuid.uuid4()}_{file.filename}"
    path = f"uploads/{folder}/{name}"
    with open(path, "wb") as f:
        f.write(file.file.read())
    return path
