import unittest
from component.MainFunction import Main


class TaxcalcTestCase(unittest.TestCase):
    def test_single_10000000(self):
        expected = 1497300;
        single_nci = Main.cal_SncIncome(10000000);
        result = Main.cal_tax(single_nci);
        self.assertEqual(expected, result);

    def test_joint_100000_8000000(self):
        expected = 1211550;
        joint_nci = Main.cal_JncIncome(100000, 8000000);
        result = Main.cal_tax(joint_nci);
        self.assertEqual(expected, result);

    def test_single_50(self):
        expected = 0;
        single_nci = Main.cal_SncIncome(50);
        result = Main.cal_tax(single_nci);
        self.assertEqual(expected, result);

    def test_single_500000(self):
        expected = 41500;
        single_nci = Main.cal_SncIncome(500000);
        result = Main.cal_tax(single_nci);
        self.assertEqual(expected, result);

    def test_single_5000000(self):
        expected = 747300;
        single_nci = Main.cal_SncIncome(5000000);
        result = Main.cal_tax(single_nci);
        self.assertEqual(expected, result);

    def test_joint_120_508(self):
        expected = 0;
        joint_nci = Main.cal_JncIncome(120, 508);
        result = Main.cal_tax(joint_nci);
        self.assertEqual(expected, result);

    def test_joint_5000000_500000(self):
        expected = 819600;
        joint_nci = Main.cal_JncIncome(5000000, 500000);
        result = Main.cal_tax(joint_nci);
        self.assertEqual(expected, result);

    def test_joint_200000_120000(self):
        expected = 800;
        joint_nci = Main.cal_JncIncome(200000, 120000);
        result = Main.cal_tax(joint_nci);
        self.assertEqual(expected, result);

    def test_joint_5000000000_120000(self):
        expected = 750014400;
        joint_nci = Main.cal_JncIncome(5000000000, 120000);
        result = Main.cal_tax(joint_nci);
        self.assertEqual(expected, result);

    def test_joint_64329827942434234_23783249728327(self):
        expected = 9653041678818984;
        joint_nci = Main.cal_JncIncome(64329827942434234, 23783249728327);
        result = Main.cal_tax(joint_nci);
        self.assertEqual(expected, result);


unittest.TestLoader().loadTestsFromTestCase(TaxcalcTestCase)

if __name__ == '__main__':
    unittest.main(verbosity=2)
