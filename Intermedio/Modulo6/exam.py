#!/usr/bin/env python3
class A:
    def a(self):
        print('a')
class B:
    def b(self):
        print('b')

    #   pass
class C(A,B):
    def c(self):
        self.a()

 #   pass
o=C()
o.c()
#print(a.__a)
#print(hasattr(a,'A'))
#try:
 #   raise Exception(1,2,3)
#except Exception as e:
 #   print(len(e.args))

def I(n):
    s = ''
    for i in range(n):
        s+= '-'
        yield s
#for x in I(3):
 #   print(x,end='')
def a(x):
    def b():
        return x+x
    return b
x = a('x')
y = a('')
print(x()+y())
#class I:
 #   def __init__(self):
  #      self.s = 'abc'
   #     self.i = 0
 #   def __inter__(self):
  #      return self
   # def __next__(self):
    #    if self.i == len(self.s):
     #       raise StopIteration
      #  v = self.s[self.i]
       # self.i +=1
        #return v

#for x in I():
 #   print(x,end='')
def o(p):
    def q():
        return '*' * p
    return q
r = o(1)
s =o(2)
print(r()+s())



def f(par2,par1):
    return par2 +par1

x,y,z =3,2,1
z,y,x=x,y,z
#print(x,y,z)

def fun(x):
    return 1 if x%2 !=0 else 2
#print(fun(fun(1)))

d = {1:0,2:1,3:2,0:1}
x = 0

for y in range(len(d)):
    x=d[x]

#print(x)
#l =input()
#p =input()
#print(l+p)
#t = (1,)
#t = t[0]+t[0]
#print(t)
x =16
#while x>0:
 #   print('+',end='')
  #  x//=2
d ={'uno':1,'tres':3, 'dos':2}
#for k in sorted(d.values()):
 #   print(k, end='')
i=4
#while i>0:
    #i-=2
    #print("*")
   # if i == 2:
  #      break
 #   else: print("*")

#d ={}
#d['2'] =[1,2]
#d['1']=[3,4]

#for x in d.keys():
 #   print(d[x][1],end="")
#def ful(d,k,v):
 #   d[k]=v
#dc ={}
#print(fun(dc,'1','v'))
ls =[[c for c in range(r)]for r in range(3)]
for x in ls:
    if len(x)<2:
        print("+")

class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x=X()
z=Z()
print(isinstance(x,Z),isinstance(z,X))
