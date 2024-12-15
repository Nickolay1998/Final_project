import unittest
def Сalculations_light_Ukr(x, y, n):
    return (x - y) * n
def Сalculations_water_Ukr(p, k, u):
    return (p - k) * u
def Сalculations_summ_Ukr(light, water, trush):
    return round(light, 1) + round(water, 1) + round(trush, 1)
class TestCalculations(unittest.TestCase):
    def test_Calculations_light_Ukr(self):
        self.assertAlmostEqual(Сalculations_light_Ukr(12345, 12000, 3.90), 1345.5)
    def test_Calculations_water_Ukr(self):
        self.assertAlmostEqual(Сalculations_water_Ukr(350, 300, 2.50), 125.0)
    def test_Calculations_summ_Ukr(self):
        self.assertAlmostEqual(Сalculations_summ_Ukr(1345.5, 125.0, 60),1530.5)

if __name__ == "__main__":
    unittest.main()


