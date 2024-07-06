import tkinter as tk
from tkinter import messagebox
import pyperclip

# Function to encrypt the message
def encrypt(message):
    message_encrypted = ""
    shifts = [3, 5, 7, 2, 9]  # Unique shifts for each character
    for i, char in enumerate(message):
        char_shifted = chr(ord(char) + shifts[i % len(shifts)])
        message_encrypted += char_shifted
    return message_encrypted

# Function to decrypt the message
def decrypt(message):
    message_decrypted = ""
    shifts = [3, 5, 7, 2, 9]  # The same unique shifts for decryption
    for i, char in enumerate(message):
        char_shifted = chr(ord(char) - shifts[i % len(shifts)])
        message_decrypted += char_shifted
    return message_decrypted

# Function to copy text to the clipboard
def copy_to_clipboard(text_to_copy):
    pyperclip.copy(text_to_copy)
    messagebox.showinfo("Info", "Text copied to clipboard")

# Create a graphical interface (GUI)
root = tk.Tk()
root.title("Encryption/Decryption Program")

# Create a larger window
root.geometry("600x400")

# Create input and output fields
input_label = tk.Label(root, text="Enter the message:")
input_label.pack(pady=10)

input_text = tk.Entry(root, font=("Helvetica", 14))
input_text.pack(pady=5)

result_label = tk.Label(root, text="Result:", font=("Helvetica", 14))
result_label.pack(pady=5)

result_text = tk.Label(root, text="", font=("Helvetica", 16), relief="solid")
result_text.pack(pady=5)

# Create functions for encryption, decryption, and copying to clipboard
def encrypt_message():
    message = input_text.get()
    encrypted = encrypt(message)
    result_text.config(text=encrypted)

def decrypt_message():
    message = input_text.get()
    decrypted = decrypt(message)
    result_text.config(text=decrypted)

# Create buttons for encryption, decryption, and copying to clipboard
encrypt_button = tk.Button(root, text="Chiffrer", font=("Helvetica", 14), command=encrypt_message)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Déchiffrer", font=("Helvetica", 14), command=decrypt_message)
decrypt_button.pack(pady=10)

copy_button = tk.Button(root, text="Copier dans le presse-papiers", font=("Helvetica", 14), command=lambda: copy_to_clipboard(result_text.cget("text")))
copy_button.pack(pady=10)

# Add label at the bottom right
author_label = tk.Label(root, text="By ShortPlanet3058", anchor="e", foreground="gray")
author_label.pack(side="bottom", fill="x")

root.mainloop()
