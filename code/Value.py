import numpy as np

UP = 0
DN = 1
LT = 2
RT = 3

class Value:
    def __init__(self, size_row, size_col, input_matrix):
        self.size_row = size_row;
        self.size_col = size_col;
        self.value = np.copy(input_matrix)
    def update(self, input_policy, reward, terminal):
        new_value = np.arange(self.size_col * self.size_row, dtype = 'f').reshape(self.size_col, self.size_row)
        for i in range(0, self.size_row):
            for j in range(0, self.size_col):
                sum = 0.0
                if (i != 0):
                    sum += input_policy.policy[i][j][UP] * (self.value[i - 1][j] + reward)
                else:
                    sum += input_policy.policy[i][j][UP] * (self.value[i][j] + reward)
                if (i != self.size_row - 1):
                    sum += input_policy.policy[i][j][DN] * (self.value[i + 1][j] + reward)
                else:
                    sum += input_policy.policy[i][j][DN] * (self.value[i][j] + reward)
                if (j != 0):
                    sum += input_policy.policy[i][j][LT] * (self.value[i][j - 1] + reward)
                else:
                    sum += input_policy.policy[i][j][LT] * (self.value[i][j] + reward)
                if (j != self.size_col - 1):
                    sum += input_policy.policy[i][j][RT] * (self.value[i][j + 1] + reward)
                else:
                    sum += input_policy.policy[i][j][RT] * (self.value[i][j] + reward)
                new_value[i][j] = sum
        self.value = np.copy(new_value)
        for i, j in terminal:
            self.value[i][j] = 0.0
    def update_vi(self, terminal, reward):
        new_value = np.arange(self.size_col * self.size_row, dtype = 'f').reshape(self.size_col, self.size_row)
        equal = True
        for i in range(0, self.size_row):
            for j in range(0, self.size_col):
                max = np.NINF
                if (i != 0):
                    if (self.value[i - 1][j] + reward > max):
                        max = self.value[i - 1][j] + reward
                else:
                    if (self.value[i][j] + reward > max):
                        max = self.value[i][j] + reward
                if (i != self.size_row - 1):
                    if (self.value[i + 1][j] + reward > max):
                        max = self.value[i + 1][j] + reward
                else:
                    if (self.value[i][j] + reward > max):
                        max = self.value[i][j] + reward
                if (j != 0):
                    if (self.value[i][j - 1] + reward > max):
                        max = self.value[i][j - 1] + reward
                else:
                    if (self.value[i][j] + reward > max):
                        max = self.value[i][j] + reward
                if (j != self.size_col - 1):
                    if (self.value[i][j + 1] + reward > max):
                        max = self.value[i][j + 1] + reward
                else:
                    if (self.value[i][j] + reward > max):
                        max = self.value[i][j] + reward
                new_value[i][j] = max
                for k, h in terminal:
                    new_value[k][h] = 0.0
                if (round(new_value[i][j], 3) != round(self.value[i][j], 3)):
                    equal = False


        for i, j in terminal:
            new_value[i][j] = 0.0
        self.value = np.copy(new_value)
        return equal
