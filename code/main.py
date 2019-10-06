import DP
import numpy as np



if __name__ == "__main__":
    map = np.loadtxt("../testcase/case1.txt")
    terminal = np.loadtxt("../testcase/terminal.txt", dtype = 'i')
    size_row, size_col = map.shape
    it = iter(terminal)
    terminal = list(zip(it, it))
    dp =DP.DP(size_row, size_col, map, terminal, -1)
    for i in range(0, 30):
        dp.policyIteration()
        dp.plot(i)
