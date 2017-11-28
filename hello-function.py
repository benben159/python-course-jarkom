#!/usr/bin/env python

def say_hello(name):
    if name == '':
        print 'Hello :)'
    else:
        print 'Hello {}'.format(name)

nama = raw_input()
say_hello(nama)
#say_hello()
