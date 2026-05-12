# 🔒 Nexus Obfuscator

**A lightweight, custom Python obfuscator that uses zero Base64 – only XOR + hex encoding.**

Nexus Obfuscator transforms any Python script into a short, encrypted stub that decrypts and executes the original code in memory. It is designed for **educational purposes, CTF challenges, or protecting your own scripts from casual inspection**.

---

## ✨ Features

- ✅ **No Base64** – uses only XOR + hex encoding
- ✅ **Built‑in compression** (zlib) – smaller output
- ✅ **Random XOR key** per run (or fixed key if needed)
- ✅ **Single‑file output** – just Python, 
- ✅ **Fast & simple** – works with any Python 3.6+ script

---

## 📦 Requirements

- Python 3.6+
- `customtkinter`

```bash
git clone https://github.com/nexusishere1/NexusObfuscator.git
cd NexusObfuscator
