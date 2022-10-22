def decrypt(text, key, matrix):
    # determine size of the matrix and choose right version of cipher
    line = "ADFGVX" if matrix.length == 6 else "ADFGX"

    # create head of the encryption matrix
    # accorging to key, first element is position in order of key
    # E.G. KLIC -> [[0, K, ''], [1, L, ''], [2, I, ''], [3, C, '']]
    encryptionMatrix = [[idx, i, ''] for idx, i in enumerate(key)]

    # sort by second element (x[1])
    # E.G. [[0, K, ''], [1, L, ''], [2, I, ''], [3, C, '']] -> [[3, C, ''], [2, I, ''], [0, K, ''], [1, L, '']]
    encryptionMatrix.sort(key=lambda x: x[1])

    # input text to the matrix according to its order (splitted by space)
    # NOTE may cause errors if input groups are not equal to number of key letters (possible fix doable? idk)
    # E.G. GAAXAA AAXFXA XFDDADX AXDXADD -> [[3, 'C', 'GAAXAA'], [2, 'I', 'AAXFXA'], [0, 'K', 'XFDDADX'], [1, 'L', 'AXDXADD']]
    for idx, group in enumerate(text.split(" ")):
        encryptionMatrix[idx][2] = group

    # sort back by first element (x[0])
    # E.G. [[3, 'C', 'GAAXAA'], [2, 'I', 'AAXFXA'], [0, 'K', 'XFDDADX'], [1, 'L', 'AXDXADD']] -> [[0, 'K', 'XFDDADX'], [1, 'L', 'AXDXADD'], [2, 'I', 'AAXFXA'], [3, 'C', 'GAAXAA']]
    encryptionMatrix.sort(key=lambda x: x[0])

    # get text to decrypt, row by row
    # need to check for index out of range (columns may have diffenrent length)
    # first column should by allways longest
    # E.G. [[0, 'K', 'XF'], [1, 'L', 'AX'], [2, 'I', 'A'], [3, 'C', 'G']] -> XAAGFX
    textToDecrypt = ""
    for i in range(len(encryptionMatrix[0][2])):  # number of characters in first column
        for j in range(len(key)):  # number of columns in encryption matrix
            textToDecrypt += encryptionMatrix[j][2][i] if len(encryptionMatrix[j][2]) > i else ''

    # final text decryption with matrix table
    # E.G. XAAGFX --zip--> [(X,A), (A,G), (F,X)] --line--> [(4,0), (0,3), (2,4)] --matrix--> [H,0,J] -> HOJ
    decryptedText = ""
    textToDecrypt = iter(textToDecrypt)  # make it iterated to work with zip
    for pair in zip(textToDecrypt, textToDecrypt):
        decryptedText += matrix.matrix[line.index(pair[0])][line.index(pair[1])]

    return decryptedText
