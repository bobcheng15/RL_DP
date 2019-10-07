import DP
import numpy as np
import sys



if __name__ == "__main__":

    map = np.loadtxt("../testcase/case" + sys.argv[1] + ".txt")
    terminal = np.loadtxt("../testcase/terminal" + sys.argv[1] + ".txt", dtype = 'i')
    size_row, size_col = map.shape
    it = iter(terminal)
    terminal = list(zip(it, it))
    dp =DP.DP(size_row, size_col, map, terminal, -1)
    if (sys.argv[2] == "pi"):
        count = dp.policyIteration()
        print("Stop after " + str(count) + " iteration of policy iteration")

    else:
        count = dp.valueIteration()
        print("Stop after " + str(count) + " iteration of value iteration")
    dp.plot(sys.argv[1], sys.argv[2])
