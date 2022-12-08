from files.create_key import key_name
from cryptography.fernet import Fernet

cipher = Fernet(key_name)

def show_passwd():
    file_name = input("Enter the name of the password:\n>> ")
    file_path = ".data/passwd/" + file_name + ".txt"
    
    with open(file_path, "rb") as df:
        encrypted_data = df.read()
    
    passwd = cipher.decrypt(encrypted_data)

    print("\n" + passwd.decode())
