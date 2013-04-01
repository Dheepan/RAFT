import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Companion_Bar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Companion_Bar tests..")

#Feature testcases

    def test_t001_Companion_Bar_AddCompanion_Box(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Companion_Bar_AddCompanion_Box.png")
            raise


    def test_t002_Companion_Bar_Store(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Companion_Bar_Store.png")
            raise


    def test_t003_Companion_Bar_Inventory(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Companion_Bar_Inventory.png")
            raise


    def test_t004_Companion_Bar_PlayMap(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Companion_Bar_PlayMap.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Companion_Bar class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
