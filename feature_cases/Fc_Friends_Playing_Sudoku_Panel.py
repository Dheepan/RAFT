import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Friends_Playing_Sudoku_Panel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Friends_Playing_Sudoku_Panel tests..")

#Feature testcases

    def test_t001_Friends_Playing_Sudoku(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Friends_Playing_Sudoku.png")
            raise


    def test_t002_Friends_Playing_Sudoku_User(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Friends_Playing_Sudoku_User.png")
            raise


    def test_t003_Friends_Playing_Sudoku_Add_Companion(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Friends_Playing_Sudoku_Add_Companion.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Friends_Playing_Sudoku_Panel class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
