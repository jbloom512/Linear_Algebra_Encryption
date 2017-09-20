#!/usr/bin/env python3
import numpy as np
import Conversion
import Generate_Encryption_Key

message_to_encrypt = '"abcdefghijklmnopqrstuvwxyz., ""'
message_to_encrypt = 'This is a random test!? to see how we do, i hope well.!'
key_size = 4

def hill_cipher_algorithm(message_to_encrypt,key_size):
    success = False
    while success == False:
        message_matrix = Conversion.generate_cipher_matrix(message_to_encrypt,key_size)
        encryption_key = Generate_Encryption_Key.generate_encryption_key(key_size)
        encrypted_message = Conversion.encrypt_message(encryption_key,message_matrix)

        decryption_key = Generate_Encryption_Key.generate_decryption_key(encryption_key)
        decrypted_message = Conversion.decrypt_message(decryption_key,encrypted_message)
        print(message_matrix)
        #print(encrypted_message)
        print(decrypted_message)
        print()
        if np.array_equiv(message_matrix,decrypted_message) == True:
            print('Success!')
            success = True
        else:
            pass

message_to_encrypt = 'This is a random test!? to see how we do, i hope well.!'
key_size = 4
hill_cipher_algorithm(message_to_encrypt,key_size)


#print(encryption_key)
#print(encrypted_message)
