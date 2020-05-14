# Practice Questions
# 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
spam = 4
# assert spam > 10

# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
eggs = 'eggs'
bacon = 'EGGS'
# assert eggs.lower() != bacon.lower()

# 3. Write an assert statement that always triggers an AssertionError.
# assert 1 == 0

# 4. What are the two lines that your program must have in order to be able to call logging.debug()?
# import logging
# logging.basicConfig(level=logging.DEBUG)

# 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
# logging.basicConfig(level=logging.DEBUG, filename='filename.txt')

# 6. What are the five logging levels?
# debug info warning error critical

# 7. What line of code can you add to disable all logging messages in your program?
# logging.disable(logging.CRITICAL)

# 8. Why is using logging messages better than using print() to display the same message?
# dont have to delete at the end
# 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
#
# 10. After you click Continue, when will the debugger stop?
# at the next line of code
# 11. What is a breakpoint?
# point where you want your debugger to intentionally stop
# 12. How do you set a breakpoint on a line of code in Mu?
# click on a line
