import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
import sys
from colorama import Fore, Style

def fernet_encrypt(data, password):
    # generate encryption KEY base on the password provided!
    hash_obj = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hash_obj.update(password.encode())
    key = base64.urlsafe_b64encode(hash_obj.finalize())

    # encrypt the data
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(data.encode('utf-8'))

    # return encrypted data
    return encrypted_message.decode()


def fernet_decrypt(data, password):
    # generate encryption KEY base on the password provided!
    hash_obj = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hash_obj.update(password.encode())
    key = base64.urlsafe_b64encode(hash_obj.finalize())

    # encrypt the data
    fernet = Fernet(key)
    try:
        encrypted_message = fernet.decrypt(data.encode('utf-8'))
    except InvalidToken:
        print(Fore.RED + "Provided password is wrong! Try again...")
        sys.exit()

    # return encrypted data
    return encrypted_message.decode()


def save_data(data, path):

    with open(path, 'w') as file:
            file.write(data)
    return path


def read_data(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileExistsError:
        print(Fore.RED + "Error: Path you've givent does not exist!")
        sys.exit()
    except FileNotFoundError:
        print(Fore.RED + "Error: Path you've givent is not available!!")
        sys.exit()
    except UnicodeDecodeError:
        print(Fore.RED + Style.BRIGHT + "ENC still can not encrypt this kind of file!\nThis feature will be added soon...")
        sys.exit()