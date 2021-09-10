import numpy
import random

from config import LEARNING_RATE
from formulas import sig, inv_sig, inv_err

curr_node_id = 0

class Layer:
    def __init__(self, num_nodes, input_vals, layer_num):
        self.num_nodes = num_nodes
        self.input_vals = input_vals
        self.layer_num = layer_num
        self.weight = [[random.random() for col in range(len(input_vals))] for row in range(num_nodes)]
        self.weight_delta = [[0 for col in range(len(input_vals))] for row in range(num_nodes)]
        self.layer_net = [0 for col in range(num_nodes)]
        self.layer_out = [0 for col in range(num_nodes)]
        self.bias = (random.random() * 2) - 1

    def eval(self):
        #evaluation part
        #Get input, compute the output of layer nodes.
        #raise Exception('Implement this part.')
        # Loop layer_net and layer_out
        for i in range(self.num_nodes):
            # Add random bias value to layer_net
            self.layer_net[i] = numpy.dot(self.input_vals, numpy.transpose(self.weight[i])) + self.bias
            # Apply sigmoid function
            self.layer_out[i] = sig(self.layer_net[i])
            

    def backprop(self, other):
        #use backpropagation method to update weights
        #raise Exception('Implement this part.')
        # Run outer loop
        for j in range(len(self.weight)):
            # Run inner loop
            for k in range(len(self.weight[j])):
                # If layer_num is only one
                if self.layer_num == 1:
                    # Update current weight using derivative of neural activation function with learning rate
                    self.weight[j][k] = self.weight[j][k] - (LEARNING_RATE * other.weight_delta[0][j] * self.input_vals[k] * other.weight[0][j] * inv_sig(self.layer_out[j]))
                # If layer_num is only two
                elif self.layer_num == 2:
                    # Update current weight using derivative of neural activation function with learning rate
                    self.weight_delta[j][k] = inv_sig(self.layer_out[j]) * inv_err(self.layer_out[j], other)
                    self.weight[j][k] = self.weight[j][k] - (LEARNING_RATE * self.weight_delta[j][k] * self.input_vals[k])
                # If layer_num is neither one nor two  
                else:
                    # Pass this inner current loop
                    pass

class cfile(file):
    def __init__(self, name, mode = 'r'):
        self = file.__init__(self, name, mode)

    def w(self, string):
        self.writelines(str(string) + '\n')
        return None
