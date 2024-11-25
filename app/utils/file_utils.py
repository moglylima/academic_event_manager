import hashlib
import zipfile
import os

def generate_csv_hash(file_path: str) -> str:
    """
    Gera o hash SHA256 do arquivo CSV.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def zip_csv_file(file_path: str) -> str:
    """
    Compacta o arquivo CSV em um arquivo ZIP.
    Retorna o caminho do arquivo ZIP gerado.
    """
    zip_file_path = file_path.replace(".csv", ".zip")
    with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=os.path.basename(file_path))
    return zip_file_path
