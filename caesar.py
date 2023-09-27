def custom_caesar_decrypt(text, output):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset - output) % 26 + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    encrypted_text = "picoCTF{gvswwmrkxlivyfmgsrhnrisegl}"
    for shift_amount in range(1, 26):
        decrypted_text = custom_caesar_decrypt(encrypted_text, shift_amount)
        print(f"output {shift_amount}: {decrypted_text}")

        #picoCTF{crossingtherubiconvfhsjkou}