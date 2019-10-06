import unittest
import Policy
import Value

UP = 0
DN = 1
LT = 2
RT = 3

class testPolicy(unittest.TestCase):
    def testContructor(self):
        terminal = [(0, 0), (2, 2)]
        pl = Policy.policy(3, 3, terminal)

        self.assertAlmostEqual(pl.policy.shape[0], 3)
        self.assertAlmostEqual(pl.policy.shape[1], 3)
        self.assertAlmostEqual(pl.policy.shape[2], 4)
    def testPolicyInitializer(self):
        terminal = [(0, 0), (2, 2)]
        pl = Policy.policy(3, 3, terminal)
        self.assertAlmostEqual(pl.policy[0][0][UP], 0.0)
        self.assertAlmostEqual(pl.policy[0][0][DN], 0.0)
        self.assertAlmostEqual(pl.policy[0][0][LT], 0.0)
        self.assertAlmostEqual(pl.policy[0][0][RT], 0.0)

        self.assertAlmostEqual(pl.policy[0][1][UP], 0.25)
        self.assertAlmostEqual(pl.policy[0][1][DN], 0.25)
        self.assertAlmostEqual(pl.policy[0][1][LT], 0.25)
        self.assertAlmostEqual(pl.policy[0][1][RT], 0.25)

        self.assertAlmostEqual(pl.policy[0][2][UP], 0.25)
        self.assertAlmostEqual(pl.policy[0][2][DN], 0.25)
        self.assertAlmostEqual(pl.policy[0][2][LT], 0.25)
        self.assertAlmostEqual(pl.policy[0][2][RT], 0.25)

        self.assertAlmostEqual(pl.policy[1][0][UP], 0.25)
        self.assertAlmostEqual(pl.policy[1][0][DN], 0.25)
        self.assertAlmostEqual(pl.policy[1][0][LT], 0.25)
        self.assertAlmostEqual(pl.policy[1][0][RT], 0.25)

        self.assertAlmostEqual(pl.policy[1][1][UP], 0.25)
        self.assertAlmostEqual(pl.policy[1][1][DN], 0.25)
        self.assertAlmostEqual(pl.policy[1][1][LT], 0.25)
        self.assertAlmostEqual(pl.policy[1][1][RT], 0.25)

        self.assertAlmostEqual(pl.policy[1][2][UP], 0.25)
        self.assertAlmostEqual(pl.policy[1][2][DN], 0.25)
        self.assertAlmostEqual(pl.policy[1][2][LT], 0.25)
        self.assertAlmostEqual(pl.policy[1][2][RT], 0.25)

        self.assertAlmostEqual(pl.policy[2][0][UP], 0.25)
        self.assertAlmostEqual(pl.policy[2][0][DN], 0.25)
        self.assertAlmostEqual(pl.policy[2][0][LT], 0.25)
        self.assertAlmostEqual(pl.policy[2][0][RT], 0.25)

        self.assertAlmostEqual(pl.policy[2][1][UP], 0.25)
        self.assertAlmostEqual(pl.policy[2][1][DN], 0.25)
        self.assertAlmostEqual(pl.policy[2][1][LT], 0.25)
        self.assertAlmostEqual(pl.policy[2][1][RT], 0.25)

        self.assertAlmostEqual(pl.policy[2][2][UP], 0.0)
        self.assertAlmostEqual(pl.policy[2][2][DN], 0.0)
        self.assertAlmostEqual(pl.policy[2][2][LT], 0.0)
        self.assertAlmostEqual(pl.policy[2][2][RT], 0.0)

    def testPolicyGreedy(self):
        input_matrix = [[0., -1., -1.], [-1., -1., -1.], [-1., -1., 0.]]
        terminal = [(0, 0), (2, 2)]
        val = Value.Value(3, 3, input_matrix)
        pl = Policy.policy(3, 3, terminal)
        val.update(pl, -1, terminal)
        pl.greedy(val, terminal)

        self.assertAlmostEqual(pl.policy[0][0][UP], 0.0)
        self.assertAlmostEqual(pl.policy[0][0][DN], 0.0)
        self.assertAlmostEqual(pl.policy[0][0][LT], 0.0)
        self.assertAlmostEqual(pl.policy[0][0][RT], 0.0)

        self.assertAlmostEqual(pl.policy[0][1][UP], 0.0)
        self.assertAlmostEqual(pl.policy[0][1][DN], 0.0)
        self.assertAlmostEqual(pl.policy[0][1][LT], 1.0)
        self.assertAlmostEqual(pl.policy[0][1][RT], 0.0)

        self.assertAlmostEqual(pl.policy[0][2][UP], 0.0)
        self.assertAlmostEqual(pl.policy[0][2][DN], 0.5)
        self.assertAlmostEqual(pl.policy[0][2][LT], 0.5)
        self.assertAlmostEqual(pl.policy[0][2][RT], 0.0)

        self.assertAlmostEqual(pl.policy[1][0][UP], 1.0)
        self.assertAlmostEqual(pl.policy[1][0][DN], 0.0)
        self.assertAlmostEqual(pl.policy[1][0][LT], 0.0)
        self.assertAlmostEqual(pl.policy[1][0][RT], 0.0)

        self.assertAlmostEqual(pl.policy[1][1][UP], 0.25)
        self.assertAlmostEqual(pl.policy[1][1][DN], 0.25)
        self.assertAlmostEqual(pl.policy[1][1][LT], 0.25)
        self.assertAlmostEqual(pl.policy[1][1][RT], 0.25)

        self.assertAlmostEqual(pl.policy[1][2][UP], 0.0)
        self.assertAlmostEqual(pl.policy[1][2][DN], 1.0)
        self.assertAlmostEqual(pl.policy[1][2][LT], 0.0)
        self.assertAlmostEqual(pl.policy[1][2][RT], 0.0)

        self.assertAlmostEqual(pl.policy[2][0][UP], 0.5)
        self.assertAlmostEqual(pl.policy[2][0][DN], 0.0)
        self.assertAlmostEqual(pl.policy[2][0][LT], 0.0)
        self.assertAlmostEqual(pl.policy[2][0][RT], 0.5)

        self.assertAlmostEqual(pl.policy[2][1][UP], 0.0)
        self.assertAlmostEqual(pl.policy[2][1][DN], 0.0)
        self.assertAlmostEqual(pl.policy[2][1][LT], 0.0)
        self.assertAlmostEqual(pl.policy[2][1][RT], 1.0)

        self.assertAlmostEqual(pl.policy[2][2][UP], 0.0)
        self.assertAlmostEqual(pl.policy[2][2][DN], 0.0)
        self.assertAlmostEqual(pl.policy[2][2][LT], 0.0)
        self.assertAlmostEqual(pl.policy[2][2][RT], 0.0)






if __name__ == "__main__":
    unittest.main()
