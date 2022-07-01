class A:
    def do(self):
        print('in A')

    
class B(A):
    pass

class c:
    def do(self):
        print('in c')

        
class D(c,B):
    pass
class f(B,c):
    pass


h=f()
h.do()
in A
print(D.mro())
[<class '__main__.D'>, <class '__main__.c'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
l.do()
in c
