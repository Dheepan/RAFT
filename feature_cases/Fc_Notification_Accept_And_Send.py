import unittest
import sys
sys.path = ['..'] + sys.path
from Singleton import HashCubeAutomation
import time



class Fc_Notification_Accept_And_Send(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._h=HashCubeAutomation("Running Fc_Notification_Accept_And_Send tests..")

#Feature testcases

    def test_t001_Notifications_Popup(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t001_Notifications_Popup.png")
            raise


    def test_t002_Notifications_Popup_Close(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t002_Notifications_Popup_Close.png")
            raise


    def test_t003_Notifications_Popup_Title(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t003_Notifications_Popup_Title.png")
            raise


    def test_t004_Notifications_Popup_Item_Gift_Text(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t004_Notifications_Popup_Item_Gift_Text.png")
            raise


    def test_t005_Notifications_Popup_Item(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t005_Notifications_Popup_Item.png")
            raise


    def test_t006_Notifications_Popup_Item(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t006_Notifications_Popup_Item.png")
            raise


    def test_t007_Notifications_Popup_Item(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t007_Notifications_Popup_Item.png")
            raise


    def test_t008_Notifications_Popup_Item(self):
        h=self._h
        try:
            h.click("")
            state=h.is_displayed("")
            self.assertTrue(state)
            self.assertFalse(state)
        except:
            h.screenshot("test_t008_Notifications_Popup_Item.png")
            raise


    @classmethod
    def tearDownClass(cls):
        print "Doing Fc_Notification_Accept_And_Send class level cleanup.."
        # all cleanup method comes here

if __name__ == "__main__":
    unittest.main()
