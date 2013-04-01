import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Send_Paid_Gifts_Popup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Send_Paid_Gifts_Popup tests..")

#Feature testcases

    def test_t001_Send_Paid_Gift_Popup(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Send_Paid_Gift_Popup.png")
            raise


    def test_t002_Send_Paid_Gift_Popup_Drop_Down_List(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Send_Paid_Gift_Popup_Drop_Down_List.png")
            raise


    def test_t003_Send_Paid_Gift_Popup_Buy_Button_Click(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Send_Paid_Gift_Popup_Buy_Button_Click.png")
            raise


    def test_t004_Send_Paid_Gift_Popup_Scroll_Arrow(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Send_Paid_Gift_Popup_Scroll_Arrow.png")
            raise


    def test_t005_Send_Paid_Gift_Popup_Close(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Send_Paid_Gift_Popup_Close.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Send_Paid_Gifts_Popup class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
