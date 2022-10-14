import numpy as np


class Molejo:

    def __init__(self, numberOfMatrices):

        self.operationCalledTimes = 0
        self.matrices = []
        self.initialMatrices = []
        self.result = []

        i = 0
        m = np.random.randint(2, 5)
        n = m

        while i < numberOfMatrices:

            matrix = self.createMatrix(m, n)
            self.matrices.append(matrix)
            self.initialMatrices.append(matrix)

            i += 1

    def createMatrix(self, m, n):
        return np.random.randint(-99, 99, size=(m, n))

    def operate(self, operation):

        self.currentOperation = operation

        operation = getattr(self, operation)

        if self.validateOperation():

            operation()

            self.toCsv()

            return self.result

        else:
            print(
                'The operation couldn\'t be completed because it didn\'t pass the validation.')

    def sum(self):

        # a = self.matrices.pop(0)
        # b = self.matrices.pop(0)

        # self.matrices.insert(0, a+b)

        while len(self.matrices) >= 2:
            a = self.matrices.pop(0)
            b = self.matrices.pop(0)
            self.matrices.insert(0, a+b)

        self.result = self.matrices
        # print('\n\n#result:\n  ', self.matrices)

    def subtraction(self):

        self.operationCalledTimes = (self.operationCalledTimes + 1)

        a = self.matrices.pop(0)
        b = self.matrices.pop(0)

        self.matrices.insert(0, a-b)

        if len(self.matrices) >= 2:
            self.subtraction()
        else:
            self.result = self.matrices
            # print('\n\n#result:\n  ', self.matrices)

    def multiplication(self):

        self.operationCalledTimes = (self.operationCalledTimes + 1)

        a = self.matrices.pop(0)
        b = self.matrices.pop(0)

        self.matrices.insert(0, np.dot(a, b))

        if len(self.matrices) >= 2:
            self.multiplication()
        else:
            self.result = self.matrices
            # print('\n\n#result:\n  ', self.matrices)

    def determinant(self):

        self.operationCalledTimes = (self.operationCalledTimes + 1)

        length = len(self.matrices)

        i = 0

        while i < length:

            a = self.matrices.pop(i)
            det = np.linalg.det(a)
            self.matrices.insert(i, round(det))
            i = i + 1

        self.result = self.matrices
        # print('\n\n#result:\n  ', self.matrices)

    def inverse(self):

        self.operationCalledTimes = (self.operationCalledTimes + 1)

        length = len(self.matrices)

        i = 0

        while i < length:

            a = self.matrices.pop(i)
            inv = np.linalg.inv(a)
            self.matrices.insert(i, inv)
            i = i + 1

        self.result = self.matrices
        # print('\n\n#result:\n  ', self.matrices)

    def toCsv(self):

        if self.currentOperation == 'determinant':
            np.savetxt(self.currentOperation + ".csv",
                       self.result, delimiter=",")
        else:
            for i in self.result:
                np.savetxt(self.currentOperation +
                           ".csv", i, delimiter="   ")

    def validateOperation(self):

        if self.currentOperation == 'sum' or self.currentOperation == 'subtraction':

            lengnth = len(self.matrices)

            if lengnth < 2:
                return False

            i = 0

            while i < (lengnth - 1):

                if (np.shape(self.matrices[i]) != np.shape(self.matrices[i+1])):
                    return False
                i += 1

            return True

        elif self.currentOperation == 'multiplication':

            lengnth = len(self.matrices)

            if lengnth < 2:
                return False

            i = 0

            while i < (lengnth - 1):
                if (np.shape(self.matrices[i])[1] != np.shape(self.matrices[i+1])[0]):
                    return False
                i += 1

            return True

        elif self.currentOperation == 'determinant':

            for i in self.matrices:

                shape = np.shape(i)

                if (shape[0] != shape[1]):
                    return False

            return True

        elif self.currentOperation == 'inverse':

            self.determinant()

            if 0 in self.result:
                return False

            self.matrices = self.initialMatrices

            return True
