import unittest
import Value
import Policy

class testValue(unittest.TestCase):
    def testValueConstructor(self):
        input_matrix = []
        input_matrix = [[0., -1., -1.], [-1., -1., -1.], [-1., -1., 0.]]
        val = Value.Value(3, 3, input_matrix)

        self.assertAlmostEqual(val.value[0][0], 0)
        self.assertAlmostEqual(val.value[0][1], -1)
        self.assertAlmostEqual(val.value[0][2], -1)
        self.assertAlmostEqual(val.value[1][0], -1)
        self.assertAlmostEqual(val.value[1][1], -1)
        self.assertAlmostEqual(val.value[1][2], -1)
        self.assertAlmostEqual(val.value[2][0], -1)
        self.assertAlmostEqual(val.value[2][1], -1)
        self.assertAlmostEqual(val.value[2][2], 0)

    def testValueUpdate(self):
        input_matrix = [[0., -1., -1.], [-1., -1., -1.], [-1., -1., 0.]]
        terminal = [(0, 0), (2, 2)]
        val = Value.Value(3, 3, input_matrix)
        pl = Policy.policy(3, 3, terminal)
        val.update(pl, -1, terminal)

        self.assertAlmostEqual(val.value[0][0], 0)
        self.assertAlmostEqual(val.value[0][1], -1.75)
        self.assertAlmostEqual(val.value[0][2], -2)
        self.assertAlmostEqual(val.value[1][0], -1.75)
        self.assertAlmostEqual(val.value[1][1], -2)
        self.assertAlmostEqual(val.value[1][2], -1.75)
        self.assertAlmostEqual(val.value[2][0], -2)
        self.assertAlmostEqual(val.value[2][1], -1.75)
        self.assertAlmostEqual(val.value[2][2], 0)

    def testValueUpdate_vi(self):
        input_matrix = [[0., -1., -1.], [-1., -1., -1.], [-1., -1., 0.]]
        terminal = [(0, 0), (2, 2)]
        val = Value.Value(3, 3, input_matrix)

        val.update_vi(terminal, -1)

        self.assertAlmostEqual(val.value[0][0], 0)
        self.assertAlmostEqual(val.value[0][1], -1)
        self.assertAlmostEqual(val.value[0][2], -2)
        self.assertAlmostEqual(val.value[1][0], -1)
        self.assertAlmostEqual(val.value[1][1], -2)
        self.assertAlmostEqual(val.value[1][2], -1)
        self.assertAlmostEqual(val.value[2][0], -2)
        self.assertAlmostEqual(val.value[2][1], -1)
        self.assertAlmostEqual(val.value[2][2], 0)

if __name__ == "__main__":
    unittest.main()
