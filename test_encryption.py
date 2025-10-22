"""
Test script to verify all encryption algorithms work correctly
"""

from encryption_program import EncryptionProgram
import os

def test_all_algorithms():
    print("Testing All Encryption Algorithms")
    print("=" * 50)
    
    program = EncryptionProgram()
    test_cases = [
        "Hello World!",
        "The quick brown fox jumps over the lazy dog.",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "123 Test Message with Numbers and Symbols! @#$"
    ]
    
    success_count = 0
    total_tests = 0
    
    for i, test_message in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: '{test_message}'")
        print("-" * 30)
        
        # Test Caesar Cipher
        try:
            shift = 7
            encrypted = program.caesar_cipher(test_message, shift, True)
            decrypted = program.caesar_cipher(encrypted, shift, False)
            
            if test_message == decrypted:
                print("✓ Caesar Cipher: PASS")
                success_count += 1
            else:
                print("✗ Caesar Cipher: FAIL")
            total_tests += 1
        except Exception as e:
            print(f"✗ Caesar Cipher: ERROR - {e}")
            total_tests += 1
        
        # Test Vigenère Cipher
        try:
            key = "TESTKEY"
            encrypted = program.vigenere_cipher(test_message, key, True)
            decrypted = program.vigenere_cipher(encrypted, key, False)
            
            if test_message == decrypted:
                print("✓ Vigenère Cipher: PASS")
                success_count += 1
            else:
                print("✗ Vigenère Cipher: FAIL")
            total_tests += 1
        except Exception as e:
            print(f"✗ Vigenère Cipher: ERROR - {e}")
            total_tests += 1
        
        # Test Custom XOR Algorithm
        try:
            key = "SecretKey123"
            encrypted = program.custom_xor_cipher(test_message, key, True)
            decrypted = program.custom_xor_cipher(encrypted, key, False)
            
            if test_message == decrypted:
                print("✓ Custom XOR Algorithm: PASS")
                success_count += 1
            else:
                print("✗ Custom XOR Algorithm: FAIL")
            total_tests += 1
        except Exception as e:
            print(f"✗ Custom XOR Algorithm: ERROR - {e}")
            total_tests += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {success_count}/{total_tests} tests passed")
    print(f"Success Rate: {(success_count/total_tests)*100:.1f}%")
    
    if success_count == total_tests:
        print("🎉 All tests passed! The encryption program is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")

if __name__ == "__main__":
    test_all_algorithms()