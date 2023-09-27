import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(encoded):
    plain = ""
    for i in range(0, len(encoded), 2):
        binary = "{0:04b}{1:04b}".format(ALPHABET.index(encoded[i]), ALPHABET.index(encoded[i+1]))
        plain += chr(int(binary, 2))
    return plain

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def descifrar_mensaje(mensaje_cifrado):
    for k in ALPHABET:
        b16 = ""
        for c in mensaje_cifrado:
            b16 += unshift(c, k)
        flag = b16_decode(b16)
        print("picoCTF{" + flag + "}")

if __name__ == "__main__":
    mensaje_cifrado = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
    descifrar_mensaje(mensaje_cifrado)
