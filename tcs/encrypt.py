def decrypt_message(key_set, encrypted_numbers):
    result = []
    for num in encrypted_numbers:
        result.append(key_set[num - 1])  # Adjust for 1-based indexing
    return "".join(result)

key_set = input("Enter the sequence of uppercase alphabets (space-separated): ").split()

encrypted_numbers = list(map(int, input("Enter the sequence of integers (space-separated): ").split()))

print("Decrypted message:", decrypt_message(key_set, encrypted_numbers))