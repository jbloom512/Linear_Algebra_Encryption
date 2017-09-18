
alphabet = 'abcdefghijklmnopqrstuvwxyz., '

#print(alphabet[23])

def Dictionary_Generation():
    
    alpha_dict = {}

    for index, value in enumerate(alphabet):

        alpha_dict[value] = index

    return alpha_dict

alpha_dict = Dictionary_Generation()
    
#Dictionary_Generation(alphabet)


def Num2Letter(number):
    
    #print(alphabet[number])
    return alphabet[number]

def Letter2Num(letter):

    #print(alpha_dict[letter.lower()])
    return alpha_dict[letter.lower()]
    


