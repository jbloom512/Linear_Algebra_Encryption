  #!/usr/bin/env python3
import numpy as np
import Conversion
import Generate_Encryption_Key

message_to_encrypt = '"abcdefghijklmnopqrstuvwxyz., ""'
message_to_encrypt = 'This is a random test!? to see how we do, i hope well.!'
key_size = 4

def hill_cipher_algorithm(message_to_encrypt,key_size):
    success = False
    count = 0
    while success == False:
        message_matrix = Conversion.generate_cipher_matrix(message_to_encrypt,key_size)
        encryption_key = Generate_Encryption_Key.generate_encryption_key(key_size)
        encrypted_message = Conversion.encrypt_message(encryption_key,message_matrix)
        decryption_key = Generate_Encryption_Key.generate_sympy_decryption_key(encryption_key)
        decrypted_message = Conversion.decrypt_message(decryption_key,encrypted_message)
        #print(message_matrix)
        #print(encrypted_message)
        #print(decrypted_message)
        if np.array_equiv(message_matrix,decrypted_message) == True:
            #print('Success')
            success = True
        else:
            pass
        count += 1

    return count

message_to_encrypt = 'This is a random test!? to see how we do, i hope well.!'
key_size = 5

# Key Size of 11 yields average of 4-5 attempts
# Anything above 11, the algorithm starts to freeze up and encounted more round off errors
# Key Size of 12 yields average of 1000+ attempts

total_attempts = []
for i in range(100):
    attempts = hill_cipher_algorithm(message_to_encrypt,key_size)
    total_attempts.append(attempts)

print(sum(total_attempts)/len(total_attempts))


#print(encryption_key)
#print(encrypted_message)
