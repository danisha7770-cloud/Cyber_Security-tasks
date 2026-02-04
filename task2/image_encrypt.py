from PIL import Image

# ---------- SETTINGS ----------
key = 50  # secret number for encryption
input_image = "input.jpeg"
encrypted_image = "encrypted.png"
decrypted_image = "decrypted.png"
# -----------------------------

# OPEN IMAGE
img = Image.open(input_image)
pixels = img.load()

width, height = img.size

# ---------- ENCRYPTION ----------
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[x, y] = (r, g, b)

img.save(encrypted_image)
print("Image encrypted successfully!")

# ---------- DECRYPTION ----------
img = Image.open(encrypted_image)
pixels = img.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        pixels[x, y] = (r, g, b)

img.save(decrypted_image)
print("Image decrypted successfully!")
