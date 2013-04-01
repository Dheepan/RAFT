import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Free_Gifts_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Free_Gifts_Popup tests..")

#Feature testcases

    def test_t001_Free_Gifts_Popup(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Free_Gifts_Popup.png")
            raise


    def test_t002_Free_Gifts_Popup_Title(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Free_Gifts_Popup_Title.png")
            raise


    def test_t003_Free_Gifts_Popup_Free_Gifts(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Free_Gifts_Popup_Free_Gifts.png")
            raise


    def test_t004_Free_Gifts_Popup_Paid_Gifts(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Free_Gifts_Popup_Paid_Gifts.png")
            raise


    def test_t005_Free_Gifts_Popup_Close(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Free_Gifts_Popup_Close.png")
            raise


    def test_t006_Free_Gifts_Popup_Free_Gift_Box_Time_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t006_Free_Gifts_Popup_Free_Gift_Box_Time_Send_Gift_Click.png")
            raise


    def test_t007_Free_Gifts_Popup_Free_Gift_Box_Gold_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t007_Free_Gifts_Popup_Free_Gift_Box_Gold_Send_Gift_Click.png")
            raise


    def test_t008_Free_Gifts_Popup_Free_Gift_Box_Undo_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t008_Free_Gifts_Popup_Free_Gift_Box_Undo_Send_Gift_Click.png")
            raise


    def test_t009_Free_Gifts_Popup_Free_Gift_Box_Surprise_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t009_Free_Gifts_Popup_Free_Gift_Box_Surprise_Send_Gift_Click.png")
            raise


    def test_t010_Free_Gifts_Popup_Free_Gift_Box_MysteryTime_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t010_Free_Gifts_Popup_Free_Gift_Box_MysteryTime_Send_Gift_Click.png")
            raise


    def test_t011_Free_Gifts_Popup_Free_Gift_Box_Time_Ask_Friends_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t011_Free_Gifts_Popup_Free_Gift_Box_Time_Ask_Friends_Click.png")
            raise


    def test_t012_Free_Gifts_Popup_Free_Gift_Box_Gold_Ask_Friends_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t012_Free_Gifts_Popup_Free_Gift_Box_Gold_Ask_Friends_Click.png")
            raise


    def test_t013_Free_Gifts_Popup_Free_Gift_Box_Undo_Ask_Friends_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t013_Free_Gifts_Popup_Free_Gift_Box_Undo_Ask_Friends_Click.png")
            raise


    def test_t014_Free_Gifts_Popup_Free_Gift_Box_Surprise_Ask_Friends_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t014_Free_Gifts_Popup_Free_Gift_Box_Surprise_Ask_Friends_Click.png")
            raise


    def test_t015_Free_Gifts_Popup_Free_Gift_Box_MysteryTime_Ask_Friends_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t015_Free_Gifts_Popup_Free_Gift_Box_MysteryTime_Ask_Friends_Click.png")
            raise


    def test_t016_Free_Gifts_Popup_Free_Gift_Box_Hint_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t016_Free_Gifts_Popup_Free_Gift_Box_Hint_Send_Gift_Click.png")
            raise


    def test_t017_Free_Gifts_Popup_Free_Gift_Box_Pause_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t017_Free_Gifts_Popup_Free_Gift_Box_Pause_Send_Gift_Click.png")
            raise


    def test_t018_Free_Gifts_Popup_Free_Gift_Box_Magic_Eye_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t018_Free_Gifts_Popup_Free_Gift_Box_Magic_Eye_Send_Gift_Click.png")
            raise


    def test_t019_Free_Gifts_Popup_Free_Gift_Box_Auto_Pencil_Send_Gift_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t019_Free_Gifts_Popup_Free_Gift_Box_Auto_Pencil_Send_Gift_Click.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Free_Gifts_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
