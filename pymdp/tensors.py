#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tensors class for named A,B,C and D
"""

class Tensors:

    def __init__(self, array, factors, variables, categories):
        self.array = array
        self.factors = factors # list of factors 
        self.variables = variables # dict of factor name -> list of variables
        self.categories = categories # dict of variable name -> list of categories

    def __getitem__(self, args):
        if not isinstance(args, tuple):
            args = (args,)
        indices = []
        for i in range(len(args)):
            arg = args[i]
            if isinstance(arg, slice):
                indices.append(arg)
            elif isinstance(arg, int):
                indices.append(arg)
            elif isinstance(arg, str):
                if i==0:
                    indices.append(self.factors.index(arg))
                else:
                    factor = self.factors[indices[0]]
                    variable = self.variables[factor][i-1]
                    indices.append(self.categories[variable].index(arg))
        
        if len(indices) == 1:
            return self.array[indices[0]]
        return self.array[indices[0]][tuple(indices[1:])]
    
    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return self.array.__iter__()

    def __next__(self):
        return self.array.__next__()