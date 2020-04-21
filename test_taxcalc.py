import unittest
from component.MainFunction import Main


class TaxcalcTestCase(unittest.TestCase):
    def test_single_10000000(self):
        expected = 1497300;
        sin_nci = Main.Single_deduc(10000000);
        result = Main.Tax_calc(sin_nci);
        self.assertEqual(expected, result);

    def test_joint_100000_8000000(self):
        expected = 1211550;
        joi_nci = Main.Joint_deduc(100000, 8000000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_800000_500000(self):
        expected = 150000;
        joi_nci = Main.Joint_deduc(800000, 500000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_256000_275000(self):
        expected = 22876.5;
        joi_nci = Main.Joint_deduc(256000, 275000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_single_50(self):
        expected = 0;
        sin_nci = Main.Single_deduc(50);
        result = Main.Tax_calc(sin_nci);
        self.assertEqual(expected, result);

    def test_single_500000(self):
        expected = 41500;
        sin_nci = Main.Single_deduc(500000);
        result = Main.Tax_calc(sin_nci);
        self.assertEqual(expected, result);

    def test_single_5000000(self):
        expected = 747300;
        sin_nci = Main.Single_deduc(5000000);
        result = Main.Tax_calc(sin_nci);
        self.assertEqual(expected, result);

    def test_joint_120_508(self):
        expected = 0;
        joi_nci = Main.Joint_deduc(120, 508);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_5000000_500000(self):
        expected = 819600;
        joi_nci = Main.Joint_deduc(5000000, 500000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_200000_120000(self):
        expected = 800;
        joi_nci = Main.Joint_deduc(200000, 120000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_603422_538743(self):
        expected = 125168.05;
        joi_nci = Main.Joint_deduc(603422, 538743);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_5000000000_120000(self):
        expected = 750014400;
        joi_nci = Main.Joint_deduc(5000000000, 120000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_5401000_3470000(self):
        expected = 1325250;
        joi_nci = Main.Joint_deduc(5401000, 3470000);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_64329827942434234_23783249728327(self):
        expected = 9653041678818984;
        joi_nci = Main.Joint_deduc(64329827942434234, 23783249728327);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

    def test_joint_39708990_34535530(self):
        expected = 11131278;
        joi_nci = Main.Joint_deduc(39708990, 34535530);
        result = Main.Tax_calc(joi_nci);
        self.assertEqual(expected, result);

unittest.TestLoader().loadTestsFromTestCase(TaxcalcTestCase)

if __name__ == '__main__':
    unittest.main(verbosity=2)
