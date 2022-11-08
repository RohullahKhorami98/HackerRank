n = int(input())
arr = map(int, input().split())
mylist = sorted(arr, reverse = True)
m = max(mylist)
newlist = [i for i in mylist if i<m]
print(newlist[0])