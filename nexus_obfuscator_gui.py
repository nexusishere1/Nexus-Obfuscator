import sys
import random
import zlib
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def generate_key():
    return random.randint(1, 255)

def encrypt(data, key):
    xored = bytes(b ^ key for b in data)
    return xored[::-1]

def build_stub(encrypted_hex, key, compress):
    return f'''import sys

_hex = "{encrypted_hex}"
_k = {key}
_data = bytes.fromhex(_hex)
_data = bytes(b ^ _k for b in _data[::-1])
exec(_data)
'''

class ObfuscatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nexus Obfuscator")
        self.geometry("600x500")

        self.input_path = ""
        self.output_path = ""

        ctk.CTkLabel(self, text="Select Python Script to Obfuscate", font=("Arial", 16)).pack(pady=20)

        self.file_frame = ctk.CTkFrame(self)
        self.file_frame.pack(pady=10, padx=20, fill="x")
        self.file_label = ctk.CTkLabel(self.file_frame, text="No file selected", wraplength=500)
        self.file_label.pack(side="left", padx=10)
        ctk.CTkButton(self.file_frame, text="Browse", command=self.select_file, width=100).pack(side="right", padx=10)

        ctk.CTkLabel(self, text="Output File Name (optional)").pack(pady=(20,0))
        self.output_entry = ctk.CTkEntry(self, width=400, placeholder_text="leave blank for input_obf.py")
        self.output_entry.pack(pady=5)

        ctk.CTkLabel(self, text="XOR Key (1-255, leave blank for random)").pack(pady=(20,0))
        self.key_entry = ctk.CTkEntry(self, width=200, placeholder_text="random")
        self.key_entry.pack(pady=5)

        self.compress_var = tk.BooleanVar(value=True)
        self.compress_check = ctk.CTkCheckBox(self, text="Enable compression (zlib)", variable=self.compress_var)
        self.compress_check.pack(pady=10)

        self.obfuscate_button = ctk.CTkButton(self, text="Obfuscate", command=self.obfuscate, state="disabled")
        self.obfuscate_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="", text_color="green")
        self.status_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path:
            self.input_path = file_path
            self.file_label.configure(text=file_path)
            self.obfuscate_button.configure(state="normal")
            if not self.output_entry.get():
                base = file_path.rsplit(".", 1)[0]
                self.output_entry.delete(0, "end")
                self.output_entry.insert(0, base + "_obf.py")

    def obfuscate(self):
        if not self.input_path:
            messagebox.showerror("Error", "No input file selected")
            return

        key_str = self.key_entry.get().strip()
        if key_str:
            try:
                key = int(key_str)
                if key < 1 or key > 255:
                    raise ValueError
            except:
                messagebox.showerror("Error", "Key must be an integer between 1 and 255")
                return
        else:
            key = generate_key()

        compress = self.compress_var.get()

        try:
            with open(self.input_path, "r", encoding="utf-8") as f:
                source = f.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read input: {e}")
            return

        source_bytes = source.encode("utf-8")
        if compress:
            source_bytes = zlib.compress(source_bytes)

        encrypted = encrypt(source_bytes, key)
        encrypted_hex = encrypted.hex()

        stub = build_stub(encrypted_hex, key, compress)

        out_path = self.output_entry.get().strip()
        if not out_path:
            out_path = self.input_path.replace(".py", "_obf.py")

        try:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(stub)
            self.status_label.configure(text=f"Success: {out_path}\nKey used: {key}", text_color="green")
            messagebox.showinfo("Done", f"Obfuscated script saved as:\n{out_path}")
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}", text_color="red")
            messagebox.showerror("Error", f"Failed to write output: {e}")

if __name__ == "__main__":
    app = ObfuscatorApp()
    app.mainloop()
