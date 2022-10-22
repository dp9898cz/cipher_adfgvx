
def encrypt(text, key, matrix):
    # determine size of the matrix and choose right version of cipher
    line = "ADFGVX" if matrix.length == 6 else "ADFGX"

    # create step one text
    # AHOJ -> GX AX GX XA (according to randomly generated matrix)
    encrypted = ""
    for i in text:
        row, col = matrix.find(i)
        encrypted += line[row] + line[col]

    # create head of the encryption matrix
    # accorging to key
    # E.G. KLIC -> [[K, ''], [L, ''], [I, ''], [C, '']]
    encryptionMatrix = [[i, ''] for i in key]

    # add text to encryption matrix (into columns)
    # create as many rows as needed
    # E.G. [[K, ''], [L, ''], [I, ''], [C, '']] -> [[K, GG], [L, XX], [I, AX], [C, XA]]
    for idx, elm in enumerate(encrypted):
        encryptionMatrix[idx % len(encryptionMatrix)][1] += elm

    # sort the matrix according to the first line (x[0] is the first element)
    # E.G. [[K, GG], [L, XX], [I, AX], [C, XA]] -> [[C, XA], [I, AX], [K, GG], [L, XX]]
    encryptionMatrix.sort(key=lambda x: x[0])

    # return text by columns
    # E.G. [[C, XA], [I, AX], [K, GG], [L, XX]] -> XA AX GG XX
    return ' '.join(x[1] for x in encryptionMatrix)
