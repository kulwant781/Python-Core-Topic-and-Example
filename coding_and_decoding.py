import random
import string

def generate_random_chars(count=3):
    """Generate a string of random characters."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(count))

def encode_message(words):
    """Encode the message based on the rules."""
    encoded_words = []
    for word in words:
        if len(word) >= 3:
            r1 = generate_random_chars()
            print(r1)
            r2 = generate_random_chars()
            print(r2)
            encoded_word = r1 + word[1:] + word[0] + r2
            print("textin")
            print(word[1:] ,word[0] + r2)
            encoded_words.append(encoded_word)
        else:
            encoded_words.append(word[::-1])
    return " ".join(encoded_words)

def decode_message(words):
    """Decode the message based on the rules."""
    decoded_words = []
    for word in words:
        if len(word) >= 9:  # Minimum length after encoding
            core_word = word[3:-3]
            decoded_word = core_word[-1] + core_word[:-1]
            decoded_words.append(decoded_word)
        else:
            decoded_words.append(word[::-1])
    return " ".join(decoded_words)

# Main program
st = input("Enter the message: ").strip()
words = st.split()
mode = input("Enter 1 for Encoding or 0 for Decoding: ").strip()

if mode == "1":
    result = encode_message(words)
    print("Encoded Message:", result)
elif mode == "0":
    result = decode_message(words)
    print("Decoded Message:", result)
else:
    print("Invalid option. Please enter 1 for Encoding or 0 for Decoding.")
