import subprocess
import threading
import time
import datetime

# unix epoch = 12am on 1st jan 1970, UTC
# time.time returns number of seconds since that time
print(time.time())

# lets make it more readablke
# ctime returns a string description of the current time
thisMoment = time.time()
print(time.ctime(thisMoment))


print("-------------------- DATETIME --------------------")
print(datetime.datetime.now())

dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt.year)
print(dt.month)
print(dt.day)

# convert time to datetime
dt = datetime.datetime.fromtimestamp(1_000_000)
dt = datetime.datetime.fromtimestamp(time.time())
print(dt)


print("-------------------- TIMEDELTA --------------------")
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days)  # counts days
print(delta.seconds)  # summs from hours down
print(delta.total_seconds())  # summs everything
print(str(delta))  # returns a nicely formatted string of above
# NOTE: there is no month/year keyword, because those are variable


print("-------------------- ARITHMETIC --------------------")
dt = datetime.datetime.now()  # note btw, this is the current time
thousandDays = datetime.timedelta(days=1000)
new_dt = dt + thousandDays
print(new_dt)

# we can pause until a certain time
# halloween2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2020:
#     print('still waiting...')
#     time.sleep(5)  # makes the computer only check the function every 5 seconds, rather than go crazy


print("-------------------- STRFTIME --------------------")
# used to convert datetime objects into nice readable strings
# "f" stands for format
oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d, %H:%M:%S'))
# NOTE that strftime does NOT begin with datetime.datetime


print("-------------------- STRPTIME --------------------")
# "p" stands for parse
dt = datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt)
# NOTE this time you do have to add datetime.datetime upfront

print(
    time.time(),
    datetime.datetime.now(),
    datetime.datetime.fromtimestamp(time.time())
)


print("-------------------- THREADING --------------------")
print('start of program')


def takeANap():
    time.sleep(5)
    print('wake up baby!')


# this function will now get executed on a separate thread
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('end of program')


# if we wanted to pass arguments too:
threadObj = threading.Thread(
    target=print,
    args=['Cats', 'Dogs', 'Frogs'],
    kwargs={'sep': '&'}
)

threadObj.start()


print("-------------------- LAUNCHING OTHER PROGRAMS --------------------")
# every instance of a program = a Process
# a single Process can have multiple threads
# two Processes cannot easily exchange variables (unlike threads)
# t = subprocess.Popen('/Applications/Telegram.app/Contents/MacOS/Telegram')  # nice so this works

# poll() # returns None if process still running and returns internal exit code if process terminated. 0 = without errors, 1 or more = with errors
# print(t.poll())  # returns None

# wait() blocks further execution until the process has terminated
# t.wait()
# print(t.poll())  # returns 0


print("-------------------- PASSING ARGUMENTS --------------------")
# typically first argument the file you want the app to open
# subprocess.Popen(['atom', '~/Dropbox/atbs/text_to_read.txt'])  # to pass arguments need a list

# to launch another python script you'll want to pass the python exec as first arg and python script as second
# subprocess.Popen(['python3', '/Users/ilja/Dropbox/atbs/17_pj_multithreaded_comics.py'])

# if we wanted to just launch the file in its default app, we'd use the open program
# subprocess.Popen(['open', '/Users/ilja/Dropbox/atbs/combinedminutes.pdf'])
