
# creating a list of permutation of input data i.e x y z
import itertools
x = int(input())
y = int(input())
z = int(input())
n = int(input())


mylist = [(xx,yy,zz) for xx in range(0,x+1) for yy in range(0,y+1) for zz in range(0,z+1)]
finallist = [list(item) for item in mylist if sum(item)!=n]
print(finallist)
