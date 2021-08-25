import string
import numpy as np

def cipher_text(plain_text):
    # make characters lowercase and remove punction and spaces
    text_normalized = "".join(char for char in plain_text.lower() if char not in string.punctuation + " ")

    # test for string size 0 or 1
    if len(text_normalized) <= 1:
        return text_normalized
    
    # find r and c (rows and columns) of text matrix (r x c) for cypher
    for c in range(2,len(text_normalized) + 2):
        if c * (c-1) >= len(text_normalized):
            r = c - 1
            break
        if c * c >= len(text_normalized):
            r = c
            break
       
    # pad string with ending spaces to match fill length of the matrix
    text_padded = text_normalized.ljust(c * r)
    
    # use numpy to change string to matrix and transpose (which is the cypher method)
    text_matrix_cyphered = np.reshape(list(text_padded),(r, c)).T
    
    # join the chars in each row then the rows with a space between and return
    return ' '.join(''.join(row) for row in text_matrix_cyphered)