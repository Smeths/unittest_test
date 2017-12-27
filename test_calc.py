import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10,5),16)
        self.assertEqual(calc.add(-2,2),0)
        self.assertEqual(calc.add(-2,-3),-5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-2,2),-4)
        self.assertEqual(calc.subtract(-2,-3),1)

    def test_mult(self):
        self.assertEqual(calc.mult(10,5),50)
        self.assertEqual(calc.mult(-2,2),-4)
        self.assertEqual(calc.mult(-2,-3),6)

    def test_div(self):
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(-2,2),-1)
        self.assertEqual(calc.div(-2,-4),0.5)

if __name__ == '__main__':
    unittest.main()
