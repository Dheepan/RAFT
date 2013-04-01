import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Store_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Store_Popup tests..")

#Feature testcases

    def test_t001_Store_Popup(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Store_Popup.png")
            raise


    def test_t002_Store_Popup_Close(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Store_Popup_Close.png")
            raise


    def test_t003_Store_Popup_Title(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Store_Popup_Title.png")
            raise


    def test_t004_Store_Popup_Presence_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Store_Popup_Presence_Pack.png")
            raise


    def test_t005_Store_Popup_Buy_Button_Combo_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Store_Popup_Buy_Button_Combo_Pack.png")
            raise


    def test_t006_Store_Popup_Buy_Button_Hint_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t006_Store_Popup_Buy_Button_Hint_Pack.png")
            raise


    def test_t007_Store_Popup_Buy_Button_Pause_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t007_Store_Popup_Buy_Button_Pause_Pack.png")
            raise


    def test_t008_Store_Popup_Buy_Button_Magiceye_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t008_Store_Popup_Buy_Button_Magiceye_Pack.png")
            raise


    def test_t009_Store_Popup_Buy_Button_Autopencil_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t009_Store_Popup_Buy_Button_Autopencil_Pack.png")
            raise


    def test_t010_Store_Popup_Buy_Button_Combo_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t010_Store_Popup_Buy_Button_Combo_Pack.png")
            raise


    def test_t011_Store_Popup_Buy_Button_Hint_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t011_Store_Popup_Buy_Button_Hint_Pack.png")
            raise


    def test_t012_Store_Popup_Buy_Button_Pause_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t012_Store_Popup_Buy_Button_Pause_Pack.png")
            raise


    def test_t013_Store_Popup_Buy_Button_Magiceye_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t013_Store_Popup_Buy_Button_Magiceye_Pack.png")
            raise


    def test_t014_Store_Popup_Buy_Button_Autopencil_Pack(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t014_Store_Popup_Buy_Button_Autopencil_Pack.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Store_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
