from matrix import Matrix
from encrypt import encrypt
from decrypt import decrypt

# matrix types: [cz, en, all]

if __name__ == "__main__":
    matrix_cz = Matrix("cz")
    matrix_en = Matrix("en")
    matrix_adfgvx = Matrix()

    print(matrix_cz.matrix)

    en_text = encrypt("AHOJJAKJE", "KLIC", matrix_cz)

    print(en_text)

    print(decrypt(en_text, "KLIC", matrix_cz))
