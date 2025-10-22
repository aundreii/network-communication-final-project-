import sys

def read_paragraph():
    print("Enter your paragraph. Press Enter on an empty line to finish:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)

def write_output(text, algorithm, mode):
    filename = "output.txt"
    header = f"Algorithm: {algorithm}\nMode: {mode}\n\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + text)
    print(f"\nOutput saved to '{filename}'")

# -------------------- Caesar Cipher --------------------
def caesar_shift_char(ch, shift):
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch

def caesar_encrypt(text, shift):
    return "".join(caesar_shift_char(ch, shift) for ch in text)

def caesar_decrypt(text, shift):
    return "".join(caesar_shift_char(ch, -shift) for ch in text)

# -------------------- Vigenère Cipher --------------------
def vigenere_key_shifts(key):
    letters = [c for c in key if c.isalpha()]
    if not letters:
        raise ValueError("Key must contain at least one alphabetic character.")
    return [ord(c.lower()) - ord('a') for c in letters]

def vigenere_process(text, key, encrypt=True):
    shifts = vigenere_key_shifts(key)
    out = []
    j = 0  # index into key shifts for alphabetic characters
    for ch in text:
        if ch.isalpha():
            s = shifts[j % len(shifts)]
            if not encrypt:
                s = -s
            out.append(caesar_shift_char(ch, s))
            j += 1
        else:
            out.append(ch)
    return "".join(out)

def vigenere_encrypt(text, key):
    return vigenere_process(text, key, encrypt=True)

def vigenere_decrypt(text, key):
    return vigenere_process(text, key, encrypt=False)

# -------------------- Rail Fence Cipher --------------------
def rail_fence_encrypt(text, rails):
    if rails < 2:
        raise ValueError("Rails must be >= 2.")
    rail = [''] * rails
    idx = 0
    step = 1
    for ch in text:
        rail[idx] += ch
        if idx == 0:
            step = 1
        elif idx == rails - 1:
            step = -1
        idx += step
    return "".join(rail)

def rail_fence_decrypt(ciphertext, rails):
    if rails < 2:
        raise ValueError("Rails must be >= 2.")
    n = len(ciphertext)
    # Build the zigzag pattern mask
    mask = [[False] * n for _ in range(rails)]
    idx = 0
    step = 1
    for col in range(n):
        mask[idx][col] = True
        if idx == 0:
            step = 1
        elif idx == rails - 1:
            step = -1
        idx += step

    # Fill characters into the mask row by row
    result = [[''] * n for _ in range(rails)]
    pos = 0
    for r in range(rails):
        for c in range(n):
            if mask[r][c]:
                result[r][c] = ciphertext[pos]
                pos += 1

    # Read off in zigzag to reconstruct plaintext
    out = []
    idx = 0
    step = 1
    for col in range(n):
        out.append(result[idx][col])
        if idx == 0:
            step = 1
        elif idx == rails - 1:
            step = -1
        idx += step
    return "".join(out)

# -------------------- CLI Flow --------------------
def choose_algorithm():
    print("\nChoose encryption algorithm:")
    print("  1 - Caesar Cipher")
    print("  2 - Vigenère Cipher")
    print("  3 - Rail Fence Cipher")
    choice = input("Enter choice (1/2/3): ").strip()
    return choice

def choose_mode():
    print("\nChoose mode:")
    print("  E - Encrypt")
    print("  D - Decrypt")
    mode = input("Enter mode (E/D): ").strip().upper()
    return mode

def get_int(prompt, allow_negative=True, min_value=None):
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if not allow_negative and val < 0:
                print("Please enter a non-negative integer.")
                continue
            if min_value is not None and val < min_value:
                print(f"Please enter an integer >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Invalid integer. Try again.")

def get_key_string(prompt, must_have_alpha=True):
    while True:
        key = input(prompt).strip()
        if must_have_alpha and not any(c.isalpha() for c in key):
            print("Key must contain at least one alphabetic character.")
            continue
        return key

def main():
    print("=== Text Encrypt/Decrypt Tool ===")
    text = read_paragraph()
    if not text:
        print("No input provided. Exiting.")
        sys.exit(0)

    alg_choice = choose_algorithm()
    mode = choose_mode()
    if mode not in ("E", "D"):
        print("Invalid mode. Exiting.")
        sys.exit(1)

    encrypting = mode == "E"

    if alg_choice == "1":
        algorithm = "Caesar"
        shift = get_int("Enter shift (e.g., 3 or -3): ", allow_negative=True)
        result = caesar_encrypt(text, shift) if encrypting else caesar_decrypt(text, shift)

    elif alg_choice == "2":
        algorithm = "Vigenère"
        key = get_key_string("Enter key (letters only recommended): ", must_have_alpha=True)
        result = vigenere_encrypt(text, key) if encrypting else vigenere_decrypt(text, key)

    elif alg_choice == "3":
        algorithm = "Rail Fence"
        rails = get_int("Enter number of rails (>=2): ", allow_negative=False, min_value=2)
        result = rail_fence_encrypt(text, rails) if encrypting else rail_fence_decrypt(text, rails)

    else:
        print("Invalid algorithm choice. Exiting.")
        sys.exit(1)

    write_output(result, algorithm, "Encrypt" if encrypting else "Decrypt")
    print("\nDone.")

if __name__ == "__main__":
    main()