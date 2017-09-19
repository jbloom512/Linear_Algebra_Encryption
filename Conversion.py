#!/usr/bin/env python3
import re
import numpy as np
import Dictionary_Generation


def sanitize(text):
    # Small bug using .strip here. If we encrypt our alphabet, we lose the space
    # at the end of the alphabet. Work around is to double quote the alphabet.
    text = text.strip().lower()
    text = re.findall(r"[a-z .,]", text)


    return text



def generate_cipher_matrix(text, size):
    # Sanitize the text - get rid of unwanted chars
    text = sanitize(text)

    # Check to see if all the text will fit into vectors of size *size*
    if len(text) % size != 0:

        # If not, we find out how many chars we need to pad our text with
        missing_chars = size - (len(text) % size)
        #print(len(text))
        #print(missing_chars)

        # Add a space (our pad) for each missing character
        for i in range(missing_chars):
            text.append(' ')

    # Define our text matrix, a counter, and a vector
    # The counter defines how many chars we have added to our pre-defined vector (initiates at 0)
    matrix = []
    count = 0
    vector = []

    # Loop through each char in our message
    for char in text:
        # Convert the character to a number using function defined in script Dictionary_Generation.py
        converted_char = Dictionary_Generation.Letter2Num(char)
        #print(char)
        # Add the converted char to the vector and increment our counter by 1
        vector.append(converted_char)
        count += 1

        # If the counter equals the desired size, add the vector to the matrix, redefine an empty vector and our counter
        if count == size:
            matrix.append(vector)
            vector = []
            count = 0
    # Convert the matrix to a numpy array
    #print(matrix)
    matrix = np.array(matrix)
    #print(matrix)

    # Because we were adding vectors as if they were rows, we take the transpose of our newly built matrix
    matrix = np.transpose(matrix)


    return matrix


def convert(key, text):
    encrypted_message = key.dot(text) % 29
    return encrypted_message

#convert(np.array([[1,2],[3,4]]), np.array([[1,2,3,4,5],[6,7,8,9,10]]))


#text="abcdefghijklmnopqrstuvwxyz., "
#generate_cipher_matrix(text,4)
#print(sanitize(text))
