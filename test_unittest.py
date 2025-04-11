import unittest
from cm_to_feet_converter import convert_cm_to_feet

class TestUnitTest(unittest.TestCase):
    def test_tests_work(self):
        self.assertEqual(2+2,4)

    def test_cm_converter_happy(self):
        self.assertEqual(convert_cm_to_feet(1), 0.0328)
        self.assertNotEqual(convert_cm_to_feet(5),100)

    def test_cm_converter_unhappy(self):
        self.assertNotEqual(convert_cm_to_feet(5),100, "5cm should not equal 100 feet")
        self.assertEqual(convert_cm_to_feet(-1), "Cannot convert negative values")

if __name__ == "__main__":
    unittest.main()