import sys

option = sys.argv[1]
if option == '-a':
    memo = sys.argv[2]
    f = open('memo3.txt', 'a')
    #print('memo')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo3.txt')
    memo = f.read()
    f.close()
    print(memo)


