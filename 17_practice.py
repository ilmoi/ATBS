# 1. What is the Unix epoch?
# jan 1st 1970
# 2. What function returns the number of seconds since the Unix epoch?
# time.time()
# 3. How can you pause your program for exactly 5 seconds?
# time.sleep(5)
# 4. What does the round() function return?
# round(num, 2) makes sure only up to 2 digits are displayed
# 5. What is the difference between a datetime object and a timedelta object?
# datetime is an actual date, timedelta is a difference object
# 6. Using the datetime module, what day of the week was January 7, 2019?
import threading
import datetime
dt = datetime.datetime.strptime('2019/01/07', '%Y/%m/%d')
print(dt)
string_dt = dt.strftime('%w')
print(string_dt)
# it returns 1 - so monday. note the counting goes like this: 0=sunday > 6=saturday

# 7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?
threadObj = threading.Thread(target=spam)
threading.start()

# 8. What should you do to avoid concurrency issues with multiple threads?
# never have multiple threads wrangle same variables at the same time. they should only use local variables from inside the function's scope.
