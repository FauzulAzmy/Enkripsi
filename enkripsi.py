import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Fungsi untuk enkripsi menggunakan Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():  # Huruf besar
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Huruf kecil
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:  # Karakter non-huruf tetap
            encrypted_text += char
    return encrypted_text

# Fungsi untuk dekripsi menggunakan Caesar Cipher
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():  # Huruf besar
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():  # Huruf kecil
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:  # Karakter non-huruf tetap
            decrypted_text += char
    return decrypted_text

# Fungsi untuk enkripsi saat tombol Enkripsi diklik
def on_encrypt():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
        encrypted_text = encrypt(text, shift)
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Nilai pergeseran harus berupa angka.")

# Fungsi untuk dekripsi saat tombol Dekripsi diklik
def on_decrypt():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
        decrypted_text = decrypt(text, shift)
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Nilai pergeseran harus berupa angka.")

# Membuat antarmuka GUI menggunakan tkinter
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x400")
root.config(bg="#2e3f4f")

# Frame utama untuk tata letak
main_frame = tk.Frame(root, bg="#2e3f4f")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Label judul
title_label = tk.Label(main_frame, text="Caesar Cipher", font=("Helvetica", 16, "bold"), bg="#2e3f4f", fg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Label dan input untuk teks yang akan dienkripsi/dekripsi
tk.Label(main_frame, text="Masukkan Teks:", font=("Helvetica", 12), bg="#2e3f4f", fg="white").grid(row=1, column=0, sticky="w", pady=5)
entry_text = tk.Text(main_frame, height=5, width=40, font=("Helvetica", 10))
entry_text.grid(row=1, column=1, pady=5, padx=10)

# Label dan input untuk nilai shift
tk.Label(main_frame, text="Nilai Pergeseran:", font=("Helvetica", 12), bg="#2e3f4f", fg="white").grid(row=2, column=0, sticky="w", pady=5)
entry_shift = tk.Entry(main_frame, width=5, font=("Helvetica", 10))
entry_shift.grid(row=2, column=1, sticky="w", padx=10)

# Tombol Enkripsi dan Dekripsi dengan gaya
btn_encrypt = ttk.Button(main_frame, text="Enkripsi", command=on_encrypt, width=15)
btn_encrypt.grid(row=3, column=0, pady=15)

btn_decrypt = ttk.Button(main_frame, text="Dekripsi", command=on_decrypt, width=15)
btn_decrypt.grid(row=3, column=1, pady=15)

# Label dan kotak teks untuk menampilkan hasil
tk.Label(main_frame, text="Hasil:", font=("Helvetica", 12), bg="#2e3f4f", fg="white").grid(row=4, column=0, sticky="w", pady=5)
entry_result = tk.Text(main_frame, height=5, width=40, font=("Helvetica", 10))
entry_result.grid(row=4, column=1, pady=5, padx=10)

# Menjalankan loop utama tkinter
root.mainloop()
