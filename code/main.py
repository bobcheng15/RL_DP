import DP
import numpy as np

# def main():
map = np.loadtxt("../testcase/case1.txt")
terminal = np.loadtxt("../testcase/terminal.txt", dtype = 'i')
size_row, size_col = map.shape
it = iter(terminal)
terminal = list(zip(it, it))
DP.DP(size_row, size_col, map, terminal, -1)    # size_row, size_col = map.shape
    # for i in range(0, size_row):
    #     for j in range(0, size_col):
    #         if ()
    # DP = DP.DP(size_row, size_col, map, )
