import tkinter as tk
from tkinter import filedialog
import tkinter.simpledialog
from tkinter import scrolledtext
import cryptography
from cryptography.fernet import Fernet


class ImageEncryptorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Encryptor")

        self.label = tk.Label(master, text="Image Encryptor", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.encrypt_button = tk.Button(master, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(master, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack(pady=10)

        self.output_text = scrolledtext.ScrolledText(master, width=40, height=10, wrap=tk.WORD)
        self.output_text.pack(pady=10)

    def encrypt_image(self):
        file_object = self.get_file_object()
        if file_object:
            try:
                file_content = file_object.read()

                key = Fernet.generate_key()
                self.save_key(key)

                encrypted_content = Fernet(key).encrypt(file_content)

                file_object.seek(0)
                file_object.write(encrypted_content)
                file_object.truncate()

                self.output_text.insert(tk.END, "Image encrypted successfully.\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {str(e)}\n")

    def decrypt_image(self):
        file_object = self.get_file_object()
        if file_object:
            try:
                file_content = file_object.read()

                key = self.load_key()

                decrypted_content = Fernet(key).decrypt(file_content)

                file_object.seek(0)
                file_object.write(decrypted_content)
                file_object.truncate()

                self.output_text.insert(tk.END, "Image decrypted successfully.\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {str(e)}\n")


    def get_file_object(self):
        file_path = tkinter.simpledialog.askstring("Select Image File", "Enter the file path:")
        return open(file_path, "r+b") if file_path else None

    def save_key(self, key):
        with open("Key.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        with open("Key.key", "rb") as key_file:
            return key_file.read()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorGUI(root)
    root.mainloop()
