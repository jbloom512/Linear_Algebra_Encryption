
alphabet = 'abcdefghijklmnopqrstuvwxyz., '


def Dictionary_Generation(alphabet):
    
    alpha_dict = {}

    for index, value in enumerate(alphabet):

        alpha_dict[value] = index

    return alpha_dict
    
#Dictionary_Generation(alphabet)
