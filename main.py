from cryptography.fernet import Fernet

def create_key():
    new_key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(new_key)
    return new_key


def get_key():
    with open('secret.key', 'rb') as key_file:
        return key_file.read()


def encrypt_text(plain_text):
    key = get_key()
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(plain_text.encode())
    return encrypted_text


def decrypt_text(encrypted_text):
    key = get_key()
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

def main():
    try:
        get_key()
    except FileNotFoundError:
        print("no key, creating key......")
        create_key()


    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message: ")
        print("2. Decrypt a message: ")
        print("3. leave?: ")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            message_to_encrypt = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_text(message_to_encrypt)
            print(f"encrypted message is: {encrypted_message.decode()}")
        elif user_choice == '2':
            message_to_decrypt = input("Enter the encrypted message: ").encode()
            decrypted_message = decrypt_text(message_to_decrypt)
            print(f"decrypted message is: {decrypted_message}")
        elif user_choice == '3':
            print("have a good day?!")
            break
        else:
            print("enter somethiing valid")


if __name__ == "__main__":
    main()