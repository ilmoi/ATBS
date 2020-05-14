import pyinputplus as pyip


def keep_busy():

    response = pyip.inputYesNo(
        'Would you like to know how to keep an idiot busy forever? Please enter yes or no: ')

    if response == 'yes':
        keep_busy()
    else:
        return


keep_busy()
