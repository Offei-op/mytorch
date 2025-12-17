from engine import Value
import random
import matplotlib.pyplot as plt



class Neuron:

    def __init__(self,xin,bias= True):
        self.w = [Value(random.uniform(-1,1)) for i in range(xin)]
        self.b = Value(random.uniform(-1,1))
        self.bias = bias
        self._params = self.w+[self.b] if bias else self.w
        
        
    def __call__(self, xs):
        assert(len(xs) == len(self.w))
        act =  sum((x*w for x, w in zip(xs,self.w)),self.b) if self.bias else sum((x*w for x, w in zip(xs,self.w))) 
        out = act.tanh()
        return out
    
    

class Layer:
    def __init__(self,xin,xout):
        self._layer = [Neuron(xin) for i in range(xout)]
        self._params = []
        for n in self._layer: 
            self._params.extend(n._params)

    def __call__(self, xs):
        out = [n(xs) for n in self._layer]
        return out if len(out) >1 else out[0]
    

class MLP:
    def __init__(self,shape):
        self._layers = [Layer(xin,xout) for xin,xout in zip(shape[:-1],shape[1:])]
        self._params = []
        for l in  self._layers:
            self._params.extend(l._params)

    def __call__(self, xs):
        x = xs
        for l in self._layers:
            x = l(x)
        return x
        
    

if __name__ == "__main__":
    XOR_IN = [[0,0],
              [0,1],
              [1,0],
              [1,1]]
    XOR_OUT = [0,
               1,
               1,
               0]   
     
    nn = MLP((2,3,1))

    it = 0
    losses = []

    while (it <2000):
        total_loss = 0
    
        for i in range(len(XOR_IN)):
            xs = XOR_IN[i]
            y_true = XOR_OUT[i]
            y_pred = nn(xs)
            loss = (y_true-y_pred)**2

            #Clear previous gradients
            for p in nn._params:
                p.grad = 0

            total_loss += loss

        #Backprop
        total_loss.backward()

        #Update parameters
        for p in nn._params:
            p.data -= 0.1 * p.grad
           
        losses.append(total_loss.data)
        it+=1



    plt.plot(losses)
    plt.show()
    print(f"{nn([0,0])}")
    print(f"{nn([0,1])}")
    print(f"{nn([1,0])}")
    print(f"{nn([1,1])}")



        