#!/usr/bin/env python3
import Conversion
import Generate_Encryption_Key

message_to_encrypt = 'abcdefghijklmnopqrstuvwxyz., '
key_size = 3


message_matrix = Conversion.generate_cipher_matrix(message_to_encrypt,key_size)
encryption_key = Generate_Encryption_Key.generate_encryption_key(key_size)

print(message_matrix)
print(encryption_key)
