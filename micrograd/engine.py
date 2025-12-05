import math
class Value:
    def __init__(self,data,_children = (), op ="",label = ""):
        self.grad = 0
        self._backward = lambda:None
        self.data = data
        self._prev  = set(_children)
        self._op = op
        self.label = label

    def __repr__(self):
        return (f"Value = {self.data}")


    def __add__(self,other):
        other = other if isinstance(other,Value) else Value(other)
        out = Value(self.data + other.data, (self,other),"+")
        def _backward():
            self.grad += out.grad * 1.0
            other.grad += out.grad * 1.0
        out._backward = _backward

        return out 
    
    def __radd__(self,other):
        return self + other
    
    def __sub__(self,other):
        return self + Value(-1)*(other)
    
    def __rsub__(self,other):
        return self-other
    
    def __mul__(self,other):
        other = other if isinstance(other,Value) else Value(other)
        out = Value(self.data * other.data, (self,other),"*")
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out 
    
    def __rmul__(self,other):
        return self * other
    
    def __pow__(self,other):
        other = other.data if isinstance(other,Value) else other       
        out = Value(self.data**other,(self,),"pow")
        
        def _backward():
            self.grad += other * self.data**(other-1) * out.grad
        out._backward = _backward
        return out
    
    def exp(self):
        out = Value(math.exp(self.data),(self,),"exp")

        def _backward():
            self.grad += out.data * out.grad
        out._backward = _backward
        return out
    
    def tanh(self):
        power = self *2
        out =   (power.exp() - 1)/(power.exp() + 1)
        def _backward():
            self.grad +=( 1 - out.data**2) * out.grad

        out._backward = _backward
        return out
    
    def __truediv__(self,other):
        out = self * other**-1
        return out
    
    def backward(self):
        self.grad = 1

        topo = []
        visited = set()

        def build_topo(v):
            visited.add(v)

            for c in v._prev:
                if c not in visited:
                    build_topo(c)

            topo.append(v)

        build_topo(self)

        for node in reversed(topo):
            node._backward()


               
        
    
















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
    
    