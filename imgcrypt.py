from PIL import Image
import numpy as np
import os

class ImageEncryptor:
    def __init__(self, key=50):
        self.key = key  # Encryption key
    
    def encrypt(self, input_path, output_path=None):
        """Encrypt an image using XOR pixel manipulation"""
        img = Image.open(input_path)
        arr = np.array(img)

        # XOR each pixel with the key
        encrypted_arr = arr ^ self.key  

        encrypted_img = Image.fromarray(encrypted_arr.astype('uint8'))

        # Preserve file format
        file_format = img.format if img.format else "PNG"
        if not output_path:
            name, ext = os.path.splitext(input_path)
            output_path = f"{name}_encrypted{ext}"

        encrypted_img.save(output_path, format=file_format)
        print(f"✅ Image encrypted and saved at {output_path}")

    def decrypt(self, input_path, output_path=None):
        """Decrypt an image (same operation as encryption)"""
        img = Image.open(input_path)
        arr = np.array(img)

        # XOR again with same key to decrypt
        decrypted_arr = arr ^ self.key  

        decrypted_img = Image.fromarray(decrypted_arr.astype('uint8'))

        # Preserve file format
        file_format = img.format if img.format else "PNG"
        if not output_path:
            name, ext = os.path.splitext(input_path)
            output_path = f"{name}_decrypted{ext}"

        decrypted_img.save(output_path, format=file_format)
        print(f"✅ Image decrypted and saved at {output_path}")


# Example usage
if __name__ == "__main__":
    tool = ImageEncryptor(key=123)
    tool.encrypt("examples/sample.png")
    tool.decrypt("examples/sample_encrypted.png")
