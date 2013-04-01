import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Puzzle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Puzzle tests..")

#Feature testcases

    def test_t001_Puzzle_Loads(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Puzzle_Loads.png")
            raise


    def test_t002_Puzzle_Scores_And_Highscores(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Puzzle_Scores_And_Highscores.png")
            raise


    def test_t003_Puzzle_Timer(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Puzzle_Timer.png")
            raise


    def test_t004_Puzzle_Puzzle_Completion_Bar(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Puzzle_Puzzle_Completion_Bar.png")
            raise


    def test_t005_Puzzle_Number_Bar(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Puzzle_Number_Bar.png")
            raise


    def test_t006_Puzzle_Music_Buttons(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t006_Puzzle_Music_Buttons.png")
            raise


    def test_t007_Puzzle_Report_A_Bug(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t007_Puzzle_Report_A_Bug.png")
            raise


    def test_t008_Puzzle_Play_Keyboard_Navigation(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t008_Puzzle_Play_Keyboard_Navigation.png")
            raise


    def test_t009_Puzzle_Play_Unrange_Values(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t009_Puzzle_Play_Unrange_Values.png")
            raise


    def test_t010_Puzzle_Back_To_Map(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t010_Puzzle_Back_To_Map.png")
            raise


    def test_t011_Puzzle_Play_Count_Unfilled_Cells(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t011_Puzzle_Play_Count_Unfilled_Cells.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Puzzle class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
