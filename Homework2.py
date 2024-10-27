import os


def start(r, w, s):
    while True:
        data = os.read(r, 100)
        data = data.decode('utf-8')
        if data[0] == 'l':
            s.add(data[1:])
        elif data[0] == 'c':
            if (data[1:] in s):
                os.write(w, b'yes')
            else:
                os.write(w, b'no')
        else:
            os.write(w, b'ok')
            return


def f():
    ls = []
    prl = []
    pwl = []
    for i in range(52):
        r, w = os.pipe()
        pwl.append(w)
        prl.append(r)
    for i in range(26):
        cur_pid = os.fork()
        if (cur_pid == 0):
            start(prl[2 * i], pwl[2 * i + 1], set())
            return 0
    while True:
        req = input()
        req = req.split()
        if (req[0] == 'load'):
            num = ord(req[1][0]) - 97
            os.write(pwl[2  * num], bytes('l' + req[1], 'utf-8'))
        elif (req[0] == 'check'):
            num = ord(req[1][0]) - 97
            os.write(pwl[2 * num], bytes('c' + req[1], 'utf-8'))
            data = os.read(prl[2 * num + 1], 3)
            print(data.decode('utf-8'))
        else:
            for i in range(26):
                os.write(pwl[2 * i], b'kill')
                data = os.read(prl[2 * i + 1], 2)
            return


f()
