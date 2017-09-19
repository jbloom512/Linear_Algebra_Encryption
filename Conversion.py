#!/usr/bin/env python3
import re


def sanitize(text):
    text = text.strip().lower()
    text = re.findall(r"[a-z .,]", text)
    return text


def generate_cipher_matrix(text, size):
    text = sanitize(text)
    matrix = []
    count = 0
    for i in range(size):
        row = []

        for num in range(size):
            row.append(text[count])
            count += 1
        matrix.append(row)
        print(matrix)
    print(matrix)
    return matrix


def convert(key, text):
    return matrix

text="Hello!?"
generate_cipher_matrix(text,3)

#print(sanitize(text))
