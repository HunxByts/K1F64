from cryptography.fernet import Fernet as fr 

def generate_kunci():
    konci = fr.generate_key()
    with open("konci.k1", 'wb') as file_konce:
        file_konce.write(konci)
