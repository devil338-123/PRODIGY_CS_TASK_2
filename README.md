# imgcrypt-simple — Pixel Manipulation Image Encryption

A minimal Python module to encrypt/decrypt images using **XOR pixel manipulation**.  
Supports **PNG, JPG, JPEG, BMP** and most formats supported by Pillow.

## Features
- Encrypt & decrypt with a single integer key.
- Preserves original image format and extension.
- Simple usage, no CLI.

## Install
```bash
pip install pillow numpy
```

## Usage
```python
from imgcrypt import ImageEncryptor

tool = ImageEncryptor(key=123)
tool.encrypt("photo.jpg")          # creates photo_encrypted.jpg
tool.decrypt("photo_encrypted.jpg")  # creates photo_encrypted_decrypted.jpg
```

## Project Structure
```
imgcrypt-simple/
├── imgcrypt.py
├── README.md
├── requirements.txt
├── LICENSE
└── examples/
    └── sample.png
```

## License
MIT License
