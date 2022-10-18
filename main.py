import Molejo


def main():

    numberOfMatrices = int(input(
        '\n\n# What is the number of matrices you want to operate with?\n\n> '))

    Molejo.Molejo(numberOfMatrices, runAllOperations=True)

    again()


def again():
    agn = input(
        '\n# Wanna...\n  1. run it again? 2. exit?\n\n> ')

    if agn == '1':
        main()
    elif agn == '2':
        exit()
    else:
        print('Sorry, didn\'t understand.')
        again()


if __name__ == '__main__':
    main()
