from random import randint

ALPHABET_CZ = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
ALPHABET_EN = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
ALPHABET_ALL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class Matrix:
    def __init__(self, matrixType=""):
        self.matrix = []
        self.setType(matrixType)

    def setType(self, matrixType):
        self.type = matrixType
        if self.type == "cz":
            self.length = 5
            self.alphabet = ALPHABET_CZ
        elif self.type == "en":
            self.length = 5
            self.alphabet = ALPHABET_EN
        else:
            self.length = 6
            self.alphabet = ALPHABET_ALL
        self.clean()
        self.fill()

    def fill(self):
        remains = self.alphabet
        for i in range(self.length):
            for j in range(self.length):
                self.matrix[i][j] = remains[randint(0, len(remains) - 1)]
                remains = remains.replace(self.matrix[i][j], '')

    def clean(self):
        self.matrix = [['' for i in range(self.length)] for j in range(self.length)]

    def find(self, letter):
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] == letter:
                    return (i, j)
