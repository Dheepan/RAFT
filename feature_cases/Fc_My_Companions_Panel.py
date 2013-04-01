import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_My_Companions_Panel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_My_Companions_Panel tests..")

#Feature testcases

    def test_t001_My_Companions_Panel(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_My_Companions_Panel.png")
            raise


    def test_t002_My_Companions_Panel_User(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_My_Companions_Panel_User.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_My_Companions_Panel class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
