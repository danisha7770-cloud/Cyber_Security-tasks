# Simple Keylogger Demo (Educational Purpose Only)

print("⚠️ This is an educational demo.")
print("Your input will be logged with your permission.\n")

text = input("Type something and press Enter: ")

file = open("keystrokes.txt", "a")
file.write(text + "\n")
file.close()

print("\nYour input has been saved to keystrokes.txt")
