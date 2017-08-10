#!/usr/bin/env python3

# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

import threading
import itertools
import time
import sys


def spin(msg, done):  # <1>
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        if done.wait(.1):  # <2>
            break  # <3>
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():  # <4>
    # pretend waiting a long time for I/O
    time.sleep(3)  # <5>
    return 42


def supervisor():  # <6>
    done = threading.Event()  # <7>
    spinner = threading.Thread(
                target=spin, args=('thinking!', done))  # <8>
    print('spinner object:', spinner)  # <9>
    spinner.start()  # <10>
    result = slow_function()  # <11>
    done.set()  # <12>
    spinner.join()  # <13>
    return result


def main():
    result = supervisor()  # <14>
    print('Answer:', result)


if __name__ == '__main__':
    main()
