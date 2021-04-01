lst =[1,2]
for v in range(2):
    lst.insert(-1,lst[v])
#print(lst)
#print(None *None)

def func(a,b):
    return b**a
#print(func(b=2,2))

list =[x*x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst

#print(fun(list))
a=1
b=0
a=a^b
b=a^b
a=a^b
#print(a,b)

nums =[1,2,3]
vals = nums
del vals[:]
#print(len(nums), len(vals), nums ==vals)
x= input()
y =input()
#print(x,y, sep="lol")
dct = {'uno': 'dos','tres':'uno','dos':'tres'}
v = dct['tres']

for k in range(len(dct)):
    v =dct[v]
#lst=[i for i in range(-1,-2)]
#print(lst)

i = 0
#while i < i+2:
#    i+=1
 #   print("*")
#else:
 #   print("*")
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
#print(tup)
dd ={"1":"0","0":"1"}
#for x in dd.vals():
#    print(x, end="")
lst =[[x for x in range(3)]for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c]%2 !=0:
            print("#")
