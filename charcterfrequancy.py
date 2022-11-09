from itertools import groupby
from itertools import chain
from collections import Counter

if __name__ == '__main__':
    inputs = input()
    inputlist = [c for c in inputs]

    groups = []
    uniquekeys = []
    data = sorted(inputlist, key=None)
    for k, g in groupby(data, None):
        groups.append(list(g))      # Store group iterator as a list
        uniquekeys.append(k)
    print("all groups:", groups)
    print("all unique keys ", uniquekeys)
    lists = []
    for i in range(len(groups)):
        lists.append(tuple([uniquekeys[i],chain.from_iterable(groups[i])]))
    print(lists)

