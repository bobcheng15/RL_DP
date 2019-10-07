import numpy as mp
import Policy
import Value
import matplotlib.pyplot as plt
import sys
class DP:
    def __init__(self, size_row, size_col, input_matrix, terminal, reward):
        self.val = Value.Value(size_row, size_col, input_matrix)
        self.pol = Policy.policy(size_row, size_col, terminal)
        self.reward = reward
        self.terminal = terminal
        self.size_col = size_col
        self.size_row = size_row
    def policyIteration(self):
        converge = False
        count = 0
        while converge == False:
            self.val.update(self.pol, self.reward, self.terminal)
            converge = self.pol.greedy(self.val, self.terminal)
            count = count + 1
            print(count)
        return count
    def valueIteration(self, times):
        converge = False
        count = 0
        while converge == False:
            converge = self.val.update_vi(self.terminal, self.reward)
            count = count + 1
        self.pol.greedy(self.val, self.terminal)
        return count

    def plot(self, argv1, argv2):
        # settings
        ax = plt.gca()
        ax.set_xlim(0, self.size_col)
        ax.set_ylim(0, self.size_row)
        miloc = plt.MultipleLocator(1)
        ax.xaxis.set_minor_locator(miloc)
        ax.yaxis.set_minor_locator(miloc)
        ax.grid(which='minor')

        # plot policy
        for i in range (0, self.size_row):
            for j in range(0, self.size_col):
                if self.pol.policy[i][j][0] != 0: plt.arrow(j+0.5, (self.size_row)-i-0.5, 0, 0.3, width=0.02)
                if self.pol.policy[i][j][1] != 0: plt.arrow(j+0.5, (self.size_row)-i-0.5, 0, -0.3, width=0.02)
                if self.pol.policy[i][j][2] != 0: plt.arrow(j+0.5, (self.size_row)-i-0.5, -0.3, 0, width=0.02)
                if self.pol.policy[i][j][3] != 0: plt.arrow(j+0.5, (self.size_row)-i-0.5, 0.3, 0, width=0.02)

        #plt.show()
        plt.savefig("../icons/result"+ argv1 + argv2 +".png")
        plt.close()
