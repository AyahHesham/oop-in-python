Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class scalculator:
    def __init__(self):
        print('welcome')
    def sum(self,x,y):
        print(x+y)
    def mull(self,a,b):
        print(a*b)
    def power(self,x,y):
        print(x**y)

        
s1=scalculator()
welcome
s1.power(4,7)
16384
x1=scalculator()
welcome
x1.sum(9,10)
19
class sscalculator(scalculator):
    def c(self,x,y):
        print(x/y)
    def cc(self,x,y):
        print(x//y)

        
d=sscalculator()
welcome
d.c(5,11)
0.45454545454545453
d.sum(20,30)
50
d.power(40,40)
12089258196146291747061760000000000000000000000000000000000000000
