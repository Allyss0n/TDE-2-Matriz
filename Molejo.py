import numpy as np
from itertools import combinations
from timeit import default_timer as timer
import csv


class Molejo:

    def __init__(self, numberOfMatrices, runAllOperations=True):

        if runAllOperations:

            self.runAllOperations(numberOfMatrices)
        else:
            self.matrices = self.createMatrices(numberOfMatrices)

            self.chooseOperation()

    # testes para ganho de perfomance
    def runAllOperations(self, numberOfMatrices):

        start = timer()
        sumResult = []
        subtractionResult = []
        productResult = []
        determinantResult = []
        inverseResult = []

        MATRICES = self.createMatrices(numberOfMatrices)

        ALL_COMBINATIONS = combinations(MATRICES, 2)

        for i in ALL_COMBINATIONS:

            A = i[0]
            B = i[1]

            shapeA = np.shape(A)
            shapeB = np.shape(B)

            if (shapeA == shapeB):
                sumResult.append(A+B)
                subtractionResult.append(A-B)

            if (shapeA[1] == shapeB[0]):
                productResult.append(np.dot(A, B))

        for i in MATRICES:

            shape = np.shape(i)

            if (shape[0] == shape[1]):
                det = round(np.linalg.det(i))
                determinantResult.append(det)

                if det != 0:
                    inverseResult.append(np.linalg.inv(i))

        if numberOfMatrices < 20:
            with open('sum.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(sumResult)
            with open('subtraction.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(subtractionResult)
            with open('product.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(productResult)
            with open('determinant.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter='\n')
                mywriter.writerow(determinantResult)
            with open('inverse.csv', 'w', newline='') as file:
                mywriter = csv.writer(file, delimiter=',')
                mywriter.writerows(inverseResult)
        else:
            np.savetxt('sum.csv', sumResult, delimiter=',',
                       fmt='%s', newline='\n\n')
            np.savetxt('subtraction.csv', subtractionResult,
                       delimiter=',', fmt='%s', newline='\n\n')
            np.savetxt('product.csv', productResult,
                       delimiter=',', fmt='%s', newline='\n\n')
            np.savetxt('determinant.csv', determinantResult,
                       delimiter=',', fmt='%s', newline='\n\n')
            np.savetxt('inverse.csv', inverseResult,
                       delimiter=',', fmt='%s', newline='\n\n')

        end = timer()

        print(
            f'\n\n\n\n\n# All done!\n\n# It tooked {(end-start)} seconds to complete all the operations.')

    def chooseOperation(self):

        options = {1: 'sum', 2: 'subtraction', 3: 'multiplication',
                   4: 'determinant', 5: 'inverse'}

        chosenOption = int(input(
            '\n\n# Now enter the number of the operation you want to perform:\n   1. Sum\n   2. Subtraction\n   3. Multiplication\n   4. Determinant\n   5. Inverse\n   6. Exit\n\n> '))

        if chosenOption == 6:
            print('Exiting the program then...')
            exit()
        elif chosenOption in options:
            self.operate(options[chosenOption])
        else:
            print('Didn\'t understand, try again...')
            self.chooseOperation()

    def createMatrices(self, numberOfMatrices):

        matrices = []

        i = 0

        while i < numberOfMatrices:
            m = np.random.randint(2, 5)
            n = np.random.randint(2, 5)

            matrices.append(np.random.randint(-99, 99, size=(m, n)))

            i += 1

        return matrices

    def operate(self, operation):

        currentOperation = operation

        operation = getattr(self, operation)

        result = operation()

        self.toCsv(currentOperation, result)

        print(result)

    def sum(self):

        allCombinations = combinations(self.matrices, 2)

        result = []

        for i in allCombinations:

            A = i[0]
            B = i[1]

            shapeA = np.shape(A)
            shapeB = np.shape(B)

            if (shapeA == shapeB):
                result.append(A+B)

        return result

    def subtraction(self):

        allCombinations = combinations(self.matrices, 2)

        result = []

        for i in allCombinations:

            A = i[0]
            B = i[1]

            shapeA = np.shape(A)
            shapeB = np.shape(B)

            if (shapeA == shapeB):
                result.append(A-B)

        return result

    def multiplication(self):

        allCombinations = combinations(self.matrices, 2)

        result = []

        for i in allCombinations:

            A = i[0]
            B = i[1]

            shapeA = np.shape(A)
            shapeB = np.shape(B)

            if (shapeA[1] == shapeB[0]):
                result.append(np.dot(A, B))

        return result

    def determinant(self):

        result = []

        for i in self.matrices:

            shape = np.shape(i)

            if (shape[0] == shape[1]):
                det = round(np.linalg.det(i))
                result.append(det)

        return result

    def inverse(self):

        result = []

        determinants = self.determinant()

        length = len(determinants)

        i = 0

        while i < length:

            shape = np.shape(self.matrices[i])

            if (shape[0] == shape[1]) and (determinants[i] != 0):
                result.append(np.linalg.inv(self.matrices[i]))

            i += 1

        return result

    def toCsv(self, currentOperation, result):
        np.savetxt(currentOperation + '.csv', result,
                   delimiter=',', fmt='%s', newline='\n\n')
