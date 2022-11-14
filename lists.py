# in this section we run commands given in comman line or userinput
if __name__ == '__main__':
    N = int(input())
    mylist = []
    for _ in range(N):
        newN = input().split()
        if newN[0] == "insert":
            mylist.insert(int(newN[1]), int(newN[2]))
        elif newN[0] == "remove":
            mylist.remove(int(newN[1]))
        elif newN[0] == "pop":
            mylist.pop()
        elif newN[0] == "append":
            mylist.append(int(newN[1]))
        elif newN[0] == "sort":
            mylist.sort()
        elif newN[0] == "reverse":
            mylist.reverse()
        elif newN[0] == "print":
            print(mylist)

