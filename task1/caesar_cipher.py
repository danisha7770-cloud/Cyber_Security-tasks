def caesar_cipher(text, shift, choice):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            if choice == "encrypt":
                new_char = chr((ord(char) - start + shift) % 26 + start)
            else:
                new_char = chr((ord(char) - start - shift) % 26 + start)

            result += new_char
        else:
            result += char

    return result


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Type encrypt or decrypt: ").lower()

output = caesar_cipher(message, shift, choice)
print("Result:", output)
