"""
Demonstration of the three encryption algorithms
This script shows how each algorithm works with examples
"""

from encryption_program import EncryptionProgram

def demonstrate_algorithms():
    print("="*60)
    print("           ENCRYPTION ALGORITHMS DEMONSTRATION")
    print("="*60)
    
    program = EncryptionProgram()
    test_message = "Hello World! This is a test message for encryption."
    
    print(f"\nTest Message: '{test_message}'")
    print("="*60)
    
    # 1. Caesar Cipher Demo
    print("\n1. CAESAR CIPHER DEMONSTRATION")
    print("-" * 40)
    shift = 5
    encrypted = program.caesar_cipher(test_message, shift, True)
    decrypted = program.caesar_cipher(encrypted, shift, False)
    
    print(f"Shift Value: {shift}")
    print(f"Original:  {test_message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Match: {test_message == decrypted}")
    
    # 2. Vigenère Cipher Demo
    print("\n2. VIGENÈRE CIPHER DEMONSTRATION")
    print("-" * 40)
    key = "SECRET"
    encrypted = program.vigenere_cipher(test_message, key, True)
    decrypted = program.vigenere_cipher(encrypted, key, False)
    
    print(f"Key: {key}")
    print(f"Original:  {test_message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Match: {test_message == decrypted}")
    
    # 3. Custom XOR Algorithm Demo
    print("\n3. CUSTOM XOR ALGORITHM DEMONSTRATION")
    print("-" * 40)
    key = "MySecretKey123"
    encrypted = program.custom_xor_cipher(test_message, key, True)
    decrypted = program.custom_xor_cipher(encrypted, key, False)
    
    print(f"Key: {key}")
    print(f"Original:  {test_message}")
    print(f"Encrypted: {repr(encrypted)}")  # Using repr to show special characters
    print(f"Decrypted: {decrypted}")
    print(f"Match: {test_message == decrypted}")
    
    print("\n" + "="*60)
    print("All algorithms successfully demonstrated!")
    print("="*60)

if __name__ == "__main__":
    demonstrate_algorithms()