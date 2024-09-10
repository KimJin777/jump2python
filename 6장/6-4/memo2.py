import sys

import sys
option = sys.argv[1]
memo = sys.argv[2]

if option == '-a':
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

    print('complete')