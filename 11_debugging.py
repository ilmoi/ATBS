import logging
import traceback

print("-------------------- RAISE --------------------")
# raise goes inside the function


def division(x, y):
    if y == 0:
        raise Exception('dividing by zero not allowed!')
    print(x/y)


# try except goes inside the execution flow
try:
    division(5, 2)
    division(3, 0)
except Exception as err:
    print(f'oh no, looks like an error has occured, {err}')


print("-------------------- HANDLING THE EXCEPTION --------------------")

try:
    raise Exception('This is an error!!!')
except:
    with open('error_file.txt', 'w') as f:
        f.write(traceback.format_exc())  # this is key
    print('written the exception to a file!')


print("-------------------- ASSERT --------------------")
L = [5, 4, 3, 2, 1]
L = sorted(L)
assert L[0] <= L[-1]  # check that first elem is smaller than last elem
# NOTE: unlike with exceptions, you should not handle assertions with try/except. If an assertion is raised - your code SHOULD crash.
# NOTE: assertions are for progammer errors, not user errors. Assertions should only fail when the program is still under development.
# NOTE: you can disable assertions when running a file like this: pyhon -O filename.py


print("-------------------- LOGGING --------------------")
# the good thing about logging vs using print statements is that you don't need to later go and find and delete all of your print statements
# you can just change the level to say logging.critical and you're good

logging.basicConfig(level=logging.DEBUG)


def sum_all_nums_up_to(x):
    total = 0
    for i in range(0, x):
        total += i
        logging.debug(f'i is {i}, total is {total}')
        # logging.info(f'i is {i}, total is {total}')
        # logging.error(f'i is {i}, total is {total}')
    return total


sum_all_nums_up_to(100)

# you can also suppress logging by passing the below. Will suppress AT that level or below and only apply to statements written below.
logging.disable(logging.INFO)
logging.info('this should NOT print')
logging.error('this SHOULD print')


print("-------------------- DEBUGGING --------------------")
# continue = execute normally until you reach a breakpoint
# step in = exercute next line of code and setp into any functions
# step over = like anove but step over any function
# step out = execute until exit current function
