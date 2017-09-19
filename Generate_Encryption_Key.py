import random
import numpy as np

mod_space = 29

'''
Generate Encryption Key
'''
# In --> size of matrix (n x n)
# Out --> List of lists [[1,2,3],[4,5,6],[7,8,9]]


def generate_encryption_key(size):
    determinant = 0
    # Need to make sure encryption key is invertible, IE det(key) != 0
    while determinant != 0:

        matrix = []

        for i in range(size):  # Repeat i times based on input size
            row = []
            for k in range(size):
                # Add Random integer from 0 - mod space that we are working in
                number = random.randint(0, mod_space)
                row.append(number)
            matrix.append(row)  # Add row to matrix

        # Convert list of lists into numpy array, which acts as a matrix
        encryption_key = np.array(matrix)

        # If matrix is invertible, end function and return matrix
        determinant = int(np.linalg.det(encryption_key))


'''
Find Modular Inverse
'''
# In --> number, modspace (default is 29 for our case)
# Out --> modular inverse of number


def modular_inverse(num):

    for i in range(mod_space):  # Loop through possibile inverses in modspace
        if (num * i) % mod_space == 1:  # If i is an inverse for the number in modspace, return the number
            return i
    return False  # If inverse does not exist, return False


'''
Generate Decryption Key
'''
# In --> Encryption Key (matrix form)
# Out --> Decryption Key


def generate_decryption_key(encryption_key):

    # Take the prod of these 2 vars
    key_inv = np.linalg.inv(encryption_key)  # Inverse of encryption key
    # Determinant of encryption key
    det_key = int(np.linalg.det(encryption_key))

    #print((key_inv * (det_key) * modular_inverse(det_key)) % 29)

    # How to get multiplicative inverse of det(key) % 29
    # If key = [[1,2],[3,4]] ,  det(key) % 29 == 27      and
    ##                         inverse(det(key) % 29) == 14
    ##
    ##
    # How do we get from 27 to 14?
    ##
    # (det_key_mod * x) % 29 = inv --> solve for x
    # x == 14 in our example

    det_key_mod = int(det_key % 29)  # Determinant of encryption key mod 29
    # Find modular inverse of above var using function defined above
    det_key_mod_inv = int(modular_inverse(det_key_mod))

    #print(det_key_mod, det_key_mod_inv)

    # Final decryption key for [[1,2],[3,4]] is [[27,1],[16,14]]
    # decryption_key = inv(det(key)mod29) * (det(key) * inv(key)) % 29
    decryption_key = (key_inv * det_key)
    #decryption_key = np.around(decryption_key)
    #decryption_key = decryption_key.astype(int)
    decryption_key = (det_key_mod_inv * decryption_key) % 29
    decryption_key = np.around(decryption_key, 0)
    print(decryption_key)
    return decryption_key


#x =  np.array([[1,2],[3,4]])
# print(x)
x = generate_encryption_key(4)
res = generate_decryption_key(x)
