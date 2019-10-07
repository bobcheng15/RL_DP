import numpy as np


UP = 0
DN = 1
LT = 2
RT = 3


class policy:
    def __init__(self, size_row, size_col, terimal):
        self.size_row = size_row;
        self.size_col = size_col;
        self.policy = np.arange(4 * size_col * size_row, dtype = 'f').reshape(size_col, size_row, 4)
        self.policy.fill(0.25)  #our policy is a 3D array
        for i, j in terimal:
            for k in range(0, 4):
                self.policy[i][j][k] = 0;
    def greedy(self, input_value, terimal):
        new_pol = np.arange(4 * self.size_col * self.size_row, dtype = 'f').reshape(self.size_col, self.size_row, 4)
        for i in range(0, self.size_row):
            for j in range(0, self.size_col):
                Return = [0., 0., 0., 0.]
                if (i != 0):
                    Return[0]= input_value.value[i - 1][j]
                else:
                    Return[0]= input_value.value[i][j]
                if (i != self.size_row - 1):
                    Return[1]= input_value.value[i + 1][j]
                else:
                    Return[1]= input_value.value[i][j]
                if (j != 0):
                    Return[2]= input_value.value[i][j - 1]
                else:
                    Return[2]= input_value.value[i][j]
                if (j != self.size_col - 1):
                    Return[3]= input_value.value[i][j + 1]
                else:
                    Return[3]= input_value.value[i][j]
                Max = max(Return)
                count = 0
                for k in range(0, 4):
                    if (Return[k] == Max):
                        count = count + 1.0
                        new_pol[i][j][k] = 1.0
                    else:
                        new_pol[i][j][k] = 0.0
                for k in range(0, 4):
                    self.policy[i][j][k] /= count
        for i, j in terimal:
            for k in range(0, 4):
                new_pol[i][j][k] = 0;
        if (np.array_equal(new_pol, self.policy)):
            return True
        else:
            self.policy = np.copy(new_pol)
            return False
