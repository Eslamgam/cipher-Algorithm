import tkinter as tk

def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            key_char = key[key_index].upper() if key[key_index].isalpha() else key[key_index]
            key_shift = ord(key_char) - ord('A' if is_upper else 'a')

            # Adjust the shift direction for decryption
            key_shift = -key_shift if decrypt else key_shift

            shifted_char = chr((ord(char) + key_shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char

            key_index = (key_index + 1) % key_length
        else:
            result += char

    return result

def encrypt_text():
    plaintext = entry_text.get()
    keyword = entry_keyword.get()
    ciphertext = vigenere_cipher(plaintext, keyword)
    result_label.config(text=f"Encrypted Text: {ciphertext}")

def decrypt_text():
    ciphertext = entry_text.get()
    keyword = entry_keyword.get()
    plaintext = vigenere_cipher(ciphertext, keyword, decrypt=True)
    result_label.config(text=f"Decrypted Text: {plaintext}")

# Create the main window
window = tk.Tk()
window.title("Vigenère Cipher GUI")

# Create and place widgets
label_text = tk.Label(window, text="Enter Text:")
label_text.pack(pady=10)

entry_text = tk.Entry(window)
entry_text.pack(pady=10)

label_keyword = tk.Label(window, text="Enter Keyword:")
label_keyword.pack(pady=10)

entry_keyword = tk.Entry(window)
entry_keyword.pack(pady=10)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
decrypt_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
