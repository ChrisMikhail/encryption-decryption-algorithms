# Caeser Cipher encryption/decryption program

def encodeOrDecode(method, message):
    letters = {i + 97: chr(ord('a') + i) for i in range(26)}
    newMsg = ""
    for char in message:    
        if char != " ":
            if method == "e" and ord(char) < 119:
                newMsg += letters[ord(char) + 4]               
            elif ord(char) > 119:
                newMsg += letters[ord(char) - 22]
            elif method == "d" and ord(char) > 100:
                newMsg += letters[ord(char) - 4]
            elif ord(char) < 100:
                newMsg += letters[ord(char) + 22]
        else:
            newMsg += " "
    return newMsg

if __name__ == "__main__":
    method = input("Hello! This is the Caesar Cipher program! Would you like to encrypt or decrypt a message? (enter e or d): ").lower()
    message = input(f"Great choice! Please enter the phrase that you want to {method} (do not include numbers or symbols except for spaces): ").lower()
    print(encodeOrDecode(method, message))
