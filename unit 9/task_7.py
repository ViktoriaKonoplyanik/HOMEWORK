import os


def create_and_encrypt_file(file_name, lines):

    with open(file_name, 'w') as f:
        f.writelines(line + '\n' for line in lines)

    with open(file_name, 'r') as f:

        file_content = f.readlines()

    encrypted_lines = []
    for line_number, line in enumerate(file_content):
        shift = line_number + 1
        encrypted_line = ''.join(
            chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.isalpha() else char
            for char in line.lower()
        )
        encrypted_lines.append(encrypted_line)

    with open(file_name, 'w') as f:
        f.writelines(encrypted_lines)

file_name = 'my_text.txt'
lines = ['Hello', 'Hello', 'Hello', 'Hello']

create_and_encrypt_file(file_name, lines)

print(f"File '{file_name}' created and encrypted.")
print('программа завершена')