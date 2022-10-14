import Molejo
from timeit import default_timer as timer


def main():

    numberOfMatrices = int(input(
        '\n\n# What is the number of matrices you want to operate with?\n\n> '))

    molejo = Molejo.Molejo(numberOfMatrices)

    options = {1: 'sum', 2: 'subtraction', 3: 'multiplication',
               4: 'determinant', 5: 'inverse', 6: 'exit'}

    chosenOption = int(input(
        '\n\n# Now enter the number of the operation you want to perform:\n   1. Sum\n   2. Subtraction\n   3. Multiplication\n   4. Determinant\n   5. Inverse\n   6. Exit\n\n> '))

    if chosenOption != 6:
        start = timer()
        result = molejo.operate(options[chosenOption])
        end = timer()
        print('\n# result:', result)
        print('\n# it tooked:', (end - start),
              'seconds to complete the operation.')

    def again(molejo):
        agn = input(
            '\n# Wanna...\n  1. run it again?\n  2. enter code? ex.: print(molejo.initialMatrices)\n  3. exit?\n\n> ')

        if agn == '1':
            main()
        elif agn == '2':
            exec(input('\n\n> '))
            again(molejo)
        elif agn == '3':
            exit()
        else:
            print('Sorry, didn\'t understand.')
            again(molejo)

    again(molejo)


if __name__ == '__main__':
    main()
