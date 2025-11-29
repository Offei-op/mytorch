class Value:
    def __init__(self,data,_children = (), op =""):
        self.grad = 1
        self.data = data
        self._children  = set(_children)
        self._op = op

    def __repr__(self):
        return (f"Value = {self.data}")


    def __add__(self,other):
        out = Value(self.data + other.data, (self,other),"+")
        self.grad = 1
        other.grad = 1
    
        return out 
    
    def __mul__(self,other):
        out = Value(self.data * other.data, (self,other),"*")
        self.grad = other.data
        other.grad = self.data
    
        return out 
    
    def backward(self):
        if not self._children:
            return None
        for child in self._children:
            child.grad = self.grad * child.grad
            child.backward()

















if __name__ == "__main__":
    a = Value(3)
    b = Value(-4)
    c = a*b
    d = Value(5)
    e = c * d

    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }")
    print(f"{d = }")
    print(f"{e = }")
    

    
    
    print(f"{a.grad=}")
    print(f"{b.grad=}")
    print(f"{c.grad=}")
    print(f"{d.grad=}")
    print(f"{e.grad=}")

    e.backward()

    print(f"{a.grad=}")
    print(f"{b.grad=}")
    print(f"{c.grad=}")
    print(f"{d.grad=}")
    print(f"{e.grad=}")
    
    