#!/usr/bin/env python2
import time


class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        # extract the file name from __file__. __file__ is proxymodules/name.py
        self.name = __file__.rsplit('/', 1)[1].split('.')[0]
        self.description = 'Log data in the module chain. Use in addition to general logging (-l/--log).'
        self.incoming = incoming  # incoming means module is on -im chain
        self.find = None  # if find is not None, this text will be highlighted
        # file: the file name, format is (in|out)-20160601-112233.13413
        self.file = ('in-' if incoming else 'out-') + \
            time.strftime('%Y%m%d-%H%M%S.') + str(time.time()).split('.')[1]
        if options is not None:
            if 'file' in options.keys():
                self.file = options['file']
        self.handle = None

    def __del__(self):
        if self.handle is not None:
            self.handle.close()

    def execute(self, data):
        if self.handle is None:
            self.handle = open(self.file, 'w', 0)  # unbuffered
            print 'Logging to file', self.file
        logentry = time.strftime('%Y%m%d-%H%M%S') + ' ' + str(time.time()) + '\n'
        logentry += data
        logentry += '-' * 20 + '\n'
        self.handle.write(logentry)
        return data

    def help(self):
        h = '\tfile: name of logfile'
        return h


if __name__ == '__main__':
    print 'This module is not supposed to be executed alone!'
