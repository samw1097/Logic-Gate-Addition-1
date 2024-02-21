import random

def gate_1 (gate_type, a, b):
# takes two inputs, a and b, and gives an output based on the logic gate type (gate_type)
# the possible gate_type values are as follows:
# | exnor: 0 | or: 1 | nand: 2 | nor: 3 | and: 4 | exor: 5 |
    gateSum= gate_type + a + b
    gateList = [0,2,3,6]
    if gateSum in gateList:
        return 1
    else:
        return 0

print (gate_1(5,1,1))