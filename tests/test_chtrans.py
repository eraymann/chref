from unittest import TestCase

from trafolta import chtrans


class Test(TestCase):
    def test_dd_to_dms(self):
        self.fail()

    def test_dmm_to_dms(self):
        d, m, s = chtrans.dmm_to_dms(46, 43.2)
        self.assertEqual(d, 46)
        self.assertEqual(m, 43)
        self.assertAlmostEqual(s, 12.0, 3)

    def test_dms_to_dd(self):
        self.fail()

    def test_dms_to_dmm(self):
        d, mm = chtrans.dms_to_dmm(46, 54, 23.123)
        self.assertEqual(d, 46)
        self.assertAlmostEqual(mm, 54.385, 3)

    def test_wgs84_to_lv95(self):
        self.fail()

    def test_string_to_dms(self):
        self.assertEqual(chtrans.string_to_dms("46°12'34.2\""), (46, 12, 34.2))
        self.assertEqual(chtrans.string_to_dms("46°12'34.2\"N"), (46, 12, 34.2))
        self.assertEqual(chtrans.string_to_dms("8°3'34\"E"), (8, 3, 34.0))
        self.assertWarns(UserWarning, chtrans.string_to_dms, "1234°3'34\"E")
        self.assertWarns(UserWarning, chtrans.string_to_dms, "bla")

    def test_dms_to_string(self):
        self.assertEqual(chtrans.dms_to_string(d=46, m=12, s=34.1238, decimals=3), "46°12'34.124\"")
        self.assertEqual(chtrans.dms_to_string(d=46, m=12, s=34, decimals=1), "46°12'34.0\"")
        self.assertEqual(chtrans.dms_to_string(d=8, m=3, s=1, decimals=1), "8°03'01.0\"")
        self.assertEqual(chtrans.dms_to_string(d=8, m=3, s=5.5, decimals=0), "8°03'06\"")

    def test_dms_to_sex(self):
        self.fail()

    def test_wgs84_to_lv03(self):
        self.fail()

    def test_lv03_to_wgs84(self):
        self.fail()

    def test_lv95_to_wgs84(self):
        self.fail()
