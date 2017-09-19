#!/usr/bin/env python3
import re
import numpy as np


def sanitize(text):
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

        # Add the char to the vector and increment our counter by 1
        vector.append(char)
        count += 1

        # If the counter equals the desired size, add the vector to the matrix, redefine an empty vector and our counter
        if count == size:
            matrix.append(vector)
            vector = []
            count = 0
    # Convert the matrix to a numpy array
    matrix = np.array(matrix)
    print(matrix)
    # Because we were adding vectors as if they were rows, we take the transpose of our newly built matrix
    matrix = np.transpose(matrix)
    print(matrix)


    return matrix


def convert(key, text):
    return matrix

text="Hey What's up hello my doods haa"
text="This is JUST!!! a test gl hf"


generate_cipher_matrix(text,3)

#print(sanitize(text))
