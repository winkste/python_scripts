import datetime

DEBUG   = 0
INFO    = 1
WARNING = 2
ERROR   = 3

levels = {0:'DEBUG', 1:'INFO', 2:'WARNING', 3:'ERROR'}


def log(level, msg):
    x = datetime.datetime.now()
    time = x.strftime('%H:%M:%S:%f')
    print(f'{time}:{levels[level]}: {msg}')

if __name__ == '__main__':
    print('log test...')
    log(DEBUG, 'this is a debug message')
    log(ERROR, 'this is a debug message')


