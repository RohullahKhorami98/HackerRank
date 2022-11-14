# solution for converting tuples to hash using hash() faction with
# user input. While uploading the code to hackerrank use pypy3 instead of python3
# otherwise it gives negative value which is wrong
if __name__ == '__main__':
    N = int(input())
    tuples = tuple(map(int, input().split()))
    t = hash(tuples)
    print(t)