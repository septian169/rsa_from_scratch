# ==========================================
# RSA FROM SCRATCH - TEXT ENCRYPTION VERSION
# ==========================================

# Cek Bilangan Prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_value, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_value, x, y


# Modular Inverse
def mod_inverse(e, phi):
    gcd_value, x, y = extended_gcd(e, phi)
    if gcd_value != 1:
        return None
    return x % phi


# Modular Exponentiation (Fast Power)
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result


# ==========================================
# MAIN PROGRAM
# ==========================================

print("========== RSA TEXT ENCRYPTION ==========")

# Input Prima
p = int(input("Masukkan bilangan prima p: "))
q = int(input("Masukkan bilangan prima q: "))

if not is_prime(p) or not is_prime(q):
    print("Error: Salah satu bukan bilangan prima!")
    exit()

# Key Generation
n = p * q
phi = (p - 1) * (q - 1)

# Pilih e
for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break

d = mod_inverse(e, phi)

print("\n=== KEY GENERATION ===")
print("n =", n)
print("phi(n) =", phi)
print("Public Key  (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

# Input plaintext
plaintext = input("\nMasukkan plaintext (teks): ")

# Enkripsi per karakter
ciphertext = []
print("\n=== PROSES ENKRIPSI ===")
for char in plaintext:
    m = ord(char)  # ubah ke ASCII
    c = mod_exp(m, e, n)
    ciphertext.append(c)
    print(f"{char} -> ASCII({m}) -> Enkripsi -> {c}")

print("\nCiphertext (list angka):")
print(ciphertext)

# Dekripsi
decrypted_text = ""
print("\n=== PROSES DEKRIPSI ===")
for c in ciphertext:
    m = mod_exp(c, d, n)
    decrypted_text += chr(m)
    print(f"{c} -> Dekripsi -> {m} -> Karakter -> {chr(m)}")

print("\nHasil Dekripsi:")
print(decrypted_text)