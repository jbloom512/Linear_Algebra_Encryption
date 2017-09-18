import random
import numpy as np

'''
Generate Encryption Key
'''
#In --> size of matrix (n x n)
#Out --> List of lists [[1,2,3],[4,5,6],[7,8,9]]

def generate_encryption_key(size):
    while True:
    # Need to make sure encryption key is invertible, IE det(key) != 0

        matrix = []

        for i in range(size):
            row = []
            for num in range(size):
                number = random.randint(0,100000000) % 29
                row.append(number)
                # Add Random integer from 0 - 100000000 % 29 to row

            matrix.append(row)
            # Add row to matrix
            # Repeat i times based on input size

        # Convert list of lists into numpy array, which acts as a matrix
        encryption_key = np.array(matrix)

        # If matrix is invertible, end function and return matrix
        if int(np.linalg.det(encryption_key)) != 0:
            print(encryption_key)
            return encryption_key
        # Otherwise, try to create another matrix until it is invertible
        else:
            pass
        

'''
Find Modular Inverse
'''
#In --> number, modspace (default is 29 for our case)
#Out --> modular inverse of number

def modular_inverse(num,mod = 29):
    
    # Loop through possibile inverses in modspace
    for i in range(mod):

        # If i is an inverse for the number in modspace, return the number
        if (num * i) % mod == 1:
            #print(i, num)
            return i
    # If inverse does not exist, return -1
    return False


'''
Generate Decryption Key
'''
#In --> Encryption Key (matrix form)
#Out --> Decryption Key

def generate_decryption_key(encryption_key):

    ## Take the prod of these 2 vars
    key_inv = np.linalg.inv(encryption_key) # Inverse of encryption key
    det_key = int(np.linalg.det(encryption_key)) # Determinant of encryption key
    
    #print((key_inv * (det_key) * modular_inverse(det_key)) % 29)
    
    ## How to get multiplicative inverse of det(key) % 29
    ## If key = [[1,2],[3,4]] ,  det(key) % 29 == 27      and
    ##                         inverse(det(key) % 29) == 14
    ##
    ##
    ## How do we get from 27 to 14?
    ##
    ## (det_key_mod * x) % 29 = inv --> solve for x
    ## x == 14 in our example


    det_key_mod = int(det_key % 29) # Determinant of encryption key mod 29
    det_key_mod_inv = int(modular_inverse(det_key_mod)) # Find modular inverse of above var using function defined above    

    #print(det_key_mod, det_key_mod_inv)


    ## Final decryption key for [[1,2],[3,4]] is [[27,1],[16,14]]
    ## decryption_key = inv(det(key)mod29) * (det(key) * inv(key)) % 29
    decryption_key = (key_inv * det_key)
    #decryption_key = np.around(decryption_key)
    #decryption_key = decryption_key.astype(int)
    decryption_key = (det_key_mod_inv * decryption_key) % 29
    decryption_key = np.around(decryption_key,0)
    print(decryption_key)
    return decryption_key
    

#x =  np.array([[1,2],[3,4]])
#print(x)
x = generate_encryption_key(4)
res = generate_decryption_key(x)
           





