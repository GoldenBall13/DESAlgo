IP_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

expansion_table = [
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
]

permutation_table = [
    15, 6, 19, 20, 28, 11, 27, 16,
    0, 14, 22, 25, 4, 17, 30, 9,
    1, 7, 23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10, 3, 24
]

input_data = "Elmiyeh"
key = "0110001001100101011010000110010101110011011010000111010001101001"

binary_data = ''.join(format(ord(char), '08b') for char in input_data)

while len(binary_data) % 64 != 0:
    binary_data += '0'
ip_output = ''.join(binary_data[i - 1] for i in IP_table)
round_key = key[:48]

expanded_data = ''.join(ip_output[i - 1] for i in expansion_table)

xor_output = ''.join(str(int(expanded_data[i - 1]) ^ int(round_key[i - 1])) for i in range(1, 49))

permutation_output = ''.join(xor_output[i - 1] for i in permutation_table)

print(f"Data:{binary_data}")
print(f"Permutation:{ip_output}")
print(f"Round key:{round_key}")
print(f"Expanded:{expanded_data}")
print(f"XOR:{xor_output}")
print(f"Permutation:{permutation_output}")
