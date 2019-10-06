import numpy as mp
import Policy
import Value

class DP:
    def __init__(self, size_row, size_col, input_matrix, terminal, reward):
        self.val = Value.Value(size_row, size_col, input_matrix)
        self.pol = Policy.policy(size_row, size_col, terminal)
        self.reward = reward
        self.terminal = terminal
    def policyIteration(self):
        self.val.update(self.pol, self.reward, self.terminal)
        self.pol.greedy(self.val, self.terminal)
