#!/usr/bin/env python3
import re


def sanitize(text):
    text = text.strip().lower()
    text = re.findall(r"[a-z .,]", text)
    return text


def generate_cipher_matrix(text, size):
    return matrix


def convert(key, text):
    return matrix

text="Hello!?"

print(sanitize(text))
