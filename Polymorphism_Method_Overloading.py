# In python we cannot call the same function or method repeatedly
# Hence using this below method for method overloading
# We can use either a!=None or a is not None



class MyClass():
    def fun(self, a=None, b=None, c=None):
        if a is not None and b is not None and c != None:
            return a + b + c
        elif a is not None and b != None:
            return a + b
        else:
            return a


obj = MyClass()
print("result is :", obj.fun(10, 20, 30))

