import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Map(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Map tests..")

#Feature testcases

    def test_t001_Map_Free_Gifts_Icon(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Map_Free_Gifts_Icon.png")
            raise


    def test_t002_Map_Milestones(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Map_Milestones.png")
            raise


    def test_t003_Map_How_To_Play_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Map_How_To_Play_Button.png")
            raise


    def test_t004_Map_Play_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Map_Play_Button.png")
            raise


    def test_t005_Map_Sudoku_Battle(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Map_Sudoku_Battle.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Map class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
