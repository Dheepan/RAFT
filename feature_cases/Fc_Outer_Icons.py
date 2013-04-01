import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Outer_Icons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Outer_Icons tests..")

#Feature testcases

    def test_t001_Outer_Icons_Sudoku_Quest(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Outer_Icons_Sudoku_Quest.png")
            raise


    def test_t002_Outer_Icons_Like_Bar(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Outer_Icons_Like_Bar.png")
            raise


    def test_t003_Outer_Icons_Number_Of_Likes(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Outer_Icons_Number_Of_Likes.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Outer_Icons class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
