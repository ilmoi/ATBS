import time


def new_lap(prev_time=None):

    try:
        now = time.time()
        readable = time.ctime(now)
        if prev_time == None:
            print('this is the first time youre launching the program.')
            print(f'current time is: {readable}')
        else:
            diff = now - prev_time
            readable = round(diff, 2)
            print(f'this much time has passed: {readable} seconds')

        a = input()
        if a == 'quit':
            exit()
        else:
            new_lap(now)
    except KeyboardInterrupt:
        # hand ctrl c
        print('\nCome back again!')


new_lap()
