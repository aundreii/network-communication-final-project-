import os
import string
from datetime import datetime

class EncryptionProgram:
    def __init__(self):
        self.algorithms = {
            '1': 'Caesar Cipher',
            '2': 'Vigenère Cipher', 
            '3': 'Custom XOR Algorithm'
        }
    
    def display_menu(self):
        print("\n" + "="*50)
        print("         DATA ENCRYPTION PROGRAM")
        print("="*50)
        print("Available Encryption Algorithms:")
        for key, value in self.algorithms.items():
            print(f"{key}. {value}")
        print("4. Exit")
        print("="*50)
    
    def get_user_input(self):
        """Get paragraph input from user"""
        print("\nEnter your message (paragraph):")
        message = input().strip()
        if not message:
            print("Error: Empty message not allowed!")
            return None
        return message
    
    def get_operation_choice(self):
        """Get encrypt/decrypt choice"""
        while True:
            choice = input("\nChoose operation:\n1. Encrypt\n2. Decrypt\nEnter choice (1/2): ").strip()
            if choice in ['1', '2']:
                return choice == '1'  # True for encrypt, False for decrypt
            print("Invalid choice! Please enter 1 or 2.")
    
    def save_to_file(self, content, algorithm_name, operation):
        """Save output to a text file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{algorithm_name.replace(' ', '_')}_{operation}_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Algorithm: {algorithm_name}\n")
                file.write(f"Operation: {operation}\n")
                file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("-" * 50 + "\n")
                file.write(content)
            
            print(f"\nOutput saved to: {filename}")
            return filename
        except Exception as e:
            print(f"Error saving file: {e}")
            return None

    # Caesar Cipher Implementation
    def caesar_cipher(self, text, shift, encrypt=True):
        """
        Caesar Cipher: Shifts each letter by a fixed number of positions
        """
        if not encrypt:
            shift = -shift
        
        result = ""
        for char in text:
            if char.isalpha():
                # Handle uppercase and lowercase separately
                ascii_offset = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - ascii_offset + shift) % 26
                result += chr(shifted + ascii_offset)
            else:
                result += char  # Keep non-alphabetic characters unchanged
        
        return result
    
    def get_caesar_shift(self):
        """Get shift value for Caesar cipher"""
        while True:
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    return shift
                print("Shift must be between 1 and 25!")
            except ValueError:
                print("Please enter a valid number!")

    # Vigenère Cipher Implementation
    def vigenere_cipher(self, text, key, encrypt=True):
        """
        Vigenère Cipher: Uses a keyword to shift letters by varying amounts
        """
        key = key.upper()
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get the shift value from the key
                shift = ord(key[key_index % len(key)]) - ord('A')
                if not encrypt:
                    shift = -shift
                
                # Apply shift
                if char.isupper():
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                
                key_index += 1
            else:
                result += char
        
        return result
    
    def get_vigenere_key(self):
        """Get key for Vigenère cipher"""
        while True:
            key = input("Enter encryption key (letters only): ").strip()
            if key and key.isalpha():
                return key.upper()
            print("Key must contain only letters and cannot be empty!")

    # Custom XOR Algorithm Implementation
    def custom_xor_cipher(self, text, key, encrypt=True):
        """
        Custom XOR Algorithm: XOR with rotating key and position-based modification
        This is a derived algorithm that combines XOR with position-based key rotation
        """
        result = ""
        key_bytes = key.encode('utf-8')
        
        for i, char in enumerate(text):
            # Rotate key based on position for added security
            key_index = i % len(key_bytes)
            rotated_key_byte = (key_bytes[key_index] + i) % 256
            
            # XOR operation
            char_code = ord(char)
            if encrypt:
                encrypted_code = char_code ^ rotated_key_byte
                # Additional transformation for encryption
                encrypted_code = (encrypted_code + i) % 256
            else:
                # Reverse the additional transformation for decryption
                decrypted_code = (char_code - i) % 256
                encrypted_code = decrypted_code ^ rotated_key_byte
            
            result += chr(encrypted_code)
        
        return result
    
    def get_xor_key(self):
        """Get key for XOR cipher"""
        while True:
            key = input("Enter encryption key (any characters): ").strip()
            if key:
                return key
            print("Key cannot be empty!")

    def run_algorithm(self, choice, message, encrypt):
        """Execute the selected encryption algorithm"""
        if choice == '1':  # Caesar Cipher
            shift = self.get_caesar_shift()
            result = self.caesar_cipher(message, shift, encrypt)
            algorithm_info = f"Caesar Cipher (Shift: {shift})"
            
        elif choice == '2':  # Vigenère Cipher
            key = self.get_vigenere_key()
            result = self.vigenere_cipher(message, key, encrypt)
            algorithm_info = f"Vigenère Cipher (Key: {key})"
            
        elif choice == '3':  # Custom XOR Algorithm
            key = self.get_xor_key()
            result = self.custom_xor_cipher(message, key, encrypt)
            algorithm_info = f"Custom XOR Algorithm (Key: {key})"
        
        return result, algorithm_info

    def run(self):
        """Main program loop"""
        print("Welcome to the Data Encryption Program!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '4':
                print("Thank you for using the Data Encryption Program!")
                break
            
            if choice not in ['1', '2', '3']:
                print("Invalid choice! Please select 1-4.")
                continue
            
            # Get input message
            message = self.get_user_input()
            if message is None:
                continue
            
            # Get operation choice
            encrypt = self.get_operation_choice()
            operation = "Encryption" if encrypt else "Decryption"
            
            try:
                # Run the selected algorithm
                result, algorithm_info = self.run_algorithm(choice, message, encrypt)
                
                # Display results
                print(f"\n{'-'*50}")
                print(f"Algorithm: {algorithm_info}")
                print(f"Operation: {operation}")
                print(f"Original: {message}")
                print(f"Result: {result}")
                print(f"{'-'*50}")
                
                # Save to file
                file_content = f"Original Message:\n{message}\n\nProcessed Message:\n{result}\n"
                self.save_to_file(file_content, self.algorithms[choice], operation)
                
            except Exception as e:
                print(f"An error occurred: {e}")
            
            # Ask if user wants to continue
            continue_choice = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("Thank you for using the Data Encryption Program!")
                break

if __name__ == "__main__":
    program = EncryptionProgram()
    program.run()