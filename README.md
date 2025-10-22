# Data Encryption Program
# note: mga ate yung file na "netcomm2(3algoSim).py" is a much simpler method the rest program whole sila na working simulataneously 
## Overview
This program implements three different encryption techniques for securing text data. It provides both encryption and decryption capabilities with a user-friendly interface.

## Implemented Algorithms

### 1. Caesar Cipher
**Type:** Substitution Cipher  
**Description:** A classic encryption technique that shifts each letter in the plaintext by a fixed number of positions in the alphabet.

**How it works:**
- Each letter is shifted by a constant value (1-25)
- Maintains case (uppercase/lowercase)
- Non-alphabetic characters remain unchanged
- Example: With shift 3, 'A' becomes 'D', 'B' becomes 'E'

**Security Level:** Low (easily breakable with frequency analysis)

### 2. Vigenère Cipher
**Type:** Polyalphabetic Substitution Cipher  
**Description:** Uses a keyword to provide different shift values for each letter, making it more secure than Caesar cipher.

**How it works:**
- Uses a repeating keyword to determine shift values
- Each letter of the keyword corresponds to a shift value
- More resistant to frequency analysis than Caesar cipher
- Example: With key "SECRET", first letter shifts by 18 (S), second by 4 (E), etc.

**Security Level:** Medium (more secure than Caesar, but still breakable with modern techniques)

### 3. Custom XOR Algorithm (Derived Algorithm)
**Type:** Stream Cipher with Position-Based Key Rotation  
**Description:** A custom algorithm that combines XOR encryption with position-based key rotation for enhanced security.

**How it works:**
- XOR operation between plaintext and a rotating key
- Key rotation based on character position adds complexity
- Additional position-based transformation for extra security
- Works with any characters (not just letters)

**Security Level:** High (for educational purposes - combines multiple techniques)

## Features

### Core Functionality
- **Input:** Accept paragraphs of any length
- **Processing:** Encrypt or decrypt using selected algorithm
- **Output:** Save results to timestamped text files
- **User Interface:** Interactive menu system

### File Output

All results are automatically saved to text files with the following naming convention:
