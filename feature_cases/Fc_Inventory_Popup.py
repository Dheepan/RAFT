import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Inventory_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Inventory_Popup tests..")

#Feature testcases

    def test_t001_Inventory_Popup(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Inventory_Popup.png")
            raise


    def test_t002_Inventory_Popup_Close(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Inventory_Popup_Close.png")
            raise


    def test_t003_Inventory_Popup_Title(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Inventory_Popup_Title.png")
            raise


    def test_t004_Inventory_Popup_Free_Gifts_Box(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Inventory_Popup_Free_Gifts_Box.png")
            raise


    def test_t005_Inventory_Popup_Paid_Gift_Box(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Inventory_Popup_Paid_Gift_Box.png")
            raise


    def test_t006_Inventory_Popup_Time_Ask_Friends_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t006_Inventory_Popup_Time_Ask_Friends_Button.png")
            raise


    def test_t007_Inventory_Popup_Gold_Ask_Friends_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t007_Inventory_Popup_Gold_Ask_Friends_Button.png")
            raise


    def test_t008_Inventory_Popup_Undo_Ask_Friends_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t008_Inventory_Popup_Undo_Ask_Friends_Button.png")
            raise


    def test_t009_Inventory_Popup_Surprise_Ask_Friends_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t009_Inventory_Popup_Surprise_Ask_Friends_Button.png")
            raise


    def test_t010_Inventory_Popup_Mystery_Time_Ask_Friends_Button(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t010_Inventory_Popup_Mystery_Time_Ask_Friends_Button.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Inventory_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
