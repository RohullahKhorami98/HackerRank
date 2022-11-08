# getting the next lowest score in the score input data
mylist = []
for _ in range(int(input())):
   name = input()
   score = float(input())
   mylist.append([name,score])

print("list before sort: " ,mylist)
mylist.sort(key = lambda x: x[1])
print("list after sort: ",mylist)
high = []
for i in range(len(mylist)):
    if mylist[i][1] != mylist[0][1]:
        high.append([mylist[i][0],mylist[i][1]])
print("list after taking out the lowest:",high)
scores = min(high,key=lambda x:x[1])
print("The scores:", scores[1])
names = []
for j in high:
    if j[1] == scores[1]:
        names.append(j[0])
print("Names:", names)
names.sort()
for k in names:
    print(k)