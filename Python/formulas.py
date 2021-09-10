import math

def sig(x):
    #use logistic function as activation function
    #raise Exception('Implement this part.')
    # Sigmoid function
    return float(1) / float(1 + math.exp(-x))

def inv_sig(x):
    #derivative of the output of neruon with respect to its input
    #raise Exception('Implement this part.')
    # Derivative of neural activation function
    return (1 - sig(x)) * sig(x)

def err(o, t):
    #squared error function, o is the actual output value and t is the target output 
    #raise Exception('Implement this part.')
    # Squared error function
    return ((t - o) ** 2) * 0.5

def inv_err(o, t):
    #derivative of squared error function with respect to o
    #raise Exception('Implement this part.')
    # Derivative of squared error function
    return (o - t)


