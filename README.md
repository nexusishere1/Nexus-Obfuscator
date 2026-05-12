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

## -- PREVIEW

https://cdn.discordapp.com/attachments/1503713833494122578/1503722518106738788/image.png?ex=6a04623a&is=6a0310ba&hm=2fe5ae05b52982bf55426c23d654a0a10a52610e99b357f29a3fd7e203f2a2e7&


## 📦 Requirements

- Python 3.6+
- `customtkinter`

```bash
git clone https://github.com/nexusishere1/NexusObfuscator.git
cd NexusObfuscator
