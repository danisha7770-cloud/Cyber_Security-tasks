# Password Complexity Checker

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1

# Check numbers
if any(char.isdigit() for char in password):
    score += 1

# Check special characters
if any(char in "!@#$%^&*()" for char in password):
    score += 1

# Final result
if score <= 2:
    print("Password Strength: WEAK ❌")
elif score == 3 or score == 4:
    print("Password Strength: MEDIUM ⚠️")
else:
    print("Password Strength: STRONG ✅")
