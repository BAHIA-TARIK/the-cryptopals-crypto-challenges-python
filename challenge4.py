import binascii

def read_file_contents(file_path): # Read file contents and remove line breaks
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except IOError:
        print("ERROR FILE IS NOT OPENED")
        return None

def convert_hex_to_bin(hexadecimal_string):
    try:
        return binascii.unhexlify(hexadecimal_string)
    except binascii.Error:
        print("ERROR")
        return None

# Decrypt ciphertext with a single-character XOR key
def decrypt_with_single_byte(ciphertext, key_char):
    return bytes([byte ^ key_char for byte in ciphertext])

# Evaluate the score of each encrypted line and detect the key
def evaluate_and_detect_key(buffered_data):
    evaluated_scores = []
    common_characters = b"ETAOIN SHRDLU"
    for idx, buffer in enumerate(buffered_data):
        for key in range(256):
            decrypted_text = decrypt_with_single_byte(buffer, key)
            if all(chr(character).isprintable() for character in decrypted_text):
                evaluation_score = sum([decrypted_text.count(character) for character in common_characters])
                evaluated_scores.append((idx, key, evaluation_score, decrypted_text))
    return sorted(evaluated_scores, key=lambda x: x[2], reverse=True)

def find_single_byte_xor_key(file_path):
    lines_from_file = read_file_contents(file_path)
    if not lines_from_file:
        return 2

    binary_buffers = [convert_hex_to_bin(line) for line in lines_from_file if convert_hex_to_bin(line)]

    evaluation_scores = evaluate_and_detect_key(binary_buffers)
    if not evaluation_scores:
        return 2

    best_score = evaluation_scores[0]
    line_index, detected_key, highest_score, decrypted_message = best_score

    hex_string = lines_from_file[line_index]
    key_in_hex = hex(detected_key)
    # displays line number, hexadecimal string, hexadecimal key, score, and decrypted message.
    print(f"Line number is: {line_index + 1}")
    print(f"Hex string is: {hex_string}")
    print(f"Key is : {key_in_hex}")
    print(f"the Score is: {highest_score}")
    print(f"the message is: {decrypted_message.decode()}")

    return 0

# Path to the file
file_location = r"C:\Users\hp\Desktop\file.txt"
find_single_byte_xor_key(file_location)
