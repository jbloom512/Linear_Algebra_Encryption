#!/usr/bin/env python3
import numpy as np
import Conversion
import Generate_Encryption_Key
import os


def write_encrypted_message(encrypted_text,decryption_key,encryption_key,dir):
    encrypted_text_file = os.path.join(dir,'Encrypted_Text.txt')
    decryption_key_file = os.path.join(dir,'Decryption_Key.txt')
    encryption_key_file = os.path.join(dir,'Encryption_Key.txt')
    with open(encrypted_text_file,'w') as file:
        file.write(encrypted_text)
    decryption_key = decryption_key.tolist()
    with open(decryption_key_file, 'w') as file:
        matrix = ''
        for row in decryption_key:
            for ele in row:
                matrix += str(int(ele)) + ' '
            matrix += '\n'
        file.write(matrix)

    encryption_key = encryption_key.tolist()
    with open(encryption_key_file, 'w') as file:
        matrix = ''
        for row in encryption_key:
            for ele in row:
                matrix += str(int(ele)) + ' '
            matrix += '\n'
        file.write(matrix)

def hill_cipher_algorithm(message_to_encrypt,key_size):
    success = False
    while success == False:
        message_matrix = Conversion.generate_cipher_matrix(message_to_encrypt,key_size)
        encryption_key = Generate_Encryption_Key.generate_encryption_key(key_size)
        print('Encryption Key:')
        print(encryption_key)
        print()
        encrypted_matrix = Conversion.encrypt_message(encryption_key,message_matrix)

        decryption_key = Generate_Encryption_Key.generate_sympy_decryption_key(encryption_key)

        print('Decryption Key:')
        print(decryption_key)
        print()
        decrypted_matrix = Conversion.decrypt_message(decryption_key,encrypted_matrix)
        if np.array_equiv(message_matrix,decrypted_matrix) == True:
            success = True
        else:
            pass
    folder = os.getcwd() + '//Encryption'
    if not os.path.exists(folder):
        os.mkdir(folder)
    encrypted_text = Conversion.convert_matrix_to_text(encrypted_matrix)
    decrypted_text = Conversion.convert_matrix_to_text(decrypted_matrix)

    print('Encrypted Text:')
    print(encrypted_text)
    print()
    print('Decrypted Text:')
    print(decrypted_text)
    write_encrypted_message(encrypted_text,decryption_key,encryption_key,folder)


#message_to_encrypt = '"abcdefghijklmnopqrstuvwxyz., ""'
#message_to_encrypt = 'This is a random test!? to see how we do, i hope well.!'
message_to_encrypt = input('What would you like to encrypt?\n')
key_size = int(input('What key Size Would you want to use?\n'))
hill_cipher_algorithm(message_to_encrypt,key_size)



#print(encryption_key)
#print(encrypted_message)
