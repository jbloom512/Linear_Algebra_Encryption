#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz., '


def Dictionary_Generation():
    alpha_dict = {}
    for index, value in enumerate(alphabet):
        alpha_dict[value] = index
    return alpha_dict

alpha_dict = Dictionary_Generation()


def Num2Letter(number):
    return alphabet[number]


def Letter2Num(letter):
    return alpha_dict[letter]
