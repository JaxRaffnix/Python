import os
print(os.getcwd())

import sys
for i in sys.argv:
    print(i)

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

import fakultaet
print(fakultaet.fakultaet.__doc__)

#dir(fakultaet)     # was macht dir?

import ackermann