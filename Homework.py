import os

def f():
    try:
        line = input()
        pid = os.fork()
        if pid == 0:
            f()
        else:
            os.wait()
            print(line)
    except EOFError:
        return


f()
