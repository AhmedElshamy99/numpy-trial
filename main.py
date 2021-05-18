import numpy as np

def randomization(n):
    A=np.random.rand(n,1)
    print(A)

def operations(h,w):
    A = np.random.random([h,w])
    B = np.random.random([h,w])
    s = A + B
    return A,B,s

def norm(A,B):
    s = np.linalg.norm(A + B)
    return s

def scalar_function(x,y):
       if x <= y:
         return x*y
       else:
         return x/y

def vector_function(x, y):
    vectors = np.vectorize(scalar_function, otypes = [float])
    return vectors


def neural_network(inputs, weights):
    z = np.tanh(weights.T.dot(inputs))
    return z


A,B,s = operations(3,4)
assert(A.shape == B.shape == s.shape)

x=int(input("enter a positive number: "))
r=randomization(x)
print(r)
